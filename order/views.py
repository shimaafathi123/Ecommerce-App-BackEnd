from .models import Order, OrderItem, User
from shopping_cart.models import Cart, CartItem
from user.models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from datetime import timedelta
from django.utils import timezone
from django.shortcuts import redirect
from django.conf import settings
import stripe
import secrets

#------------------------------------------------------
#payment
stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckout(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        user = self.request.user
        cart = Cart.objects.get(user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        
        # validation before checkout
        if not cart_items:
            return Response({"detail": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)
        for item in cart_items:
            if item.quantity > item.product.available_quantity:
                return Response({'detail': f"Sorry, we do not have enough stock for {item.product.name}"}, status=status.HTTP_400_BAD_REQUEST)

        #make checkout Session
        line_items = []
        for item in cart_items:
            product_name = item.product.name
            price = item.product.price * 100  
            line_item = {
                'price_data' :{
                    'currency' : 'usd',  
                    'product_data': {
                        'name': product_name,
                    },
                    'unit_amount': int(price)
                },
                'quantity' : item.quantity
            }
            line_items.append(line_item)
        try:
            token = secrets.token_hex(16) # generate payment token
            base_url = request.scheme + '://' + request.get_host()
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,  # include the line_items parameter here
                mode='payment',
                success_url= f'{base_url}/orders/create?token={token}&user={user.id}',
                cancel_url= f'{base_url}/orders/create',
                )
            pToken = PaymentToken(user=user,Ptoken=token,status=True)
            pToken.save()
        except AuthenticationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        # return redirect(checkout_session.url , code=303)
        return Response({'url': checkout_session.url})

#-----------------------------------------------------

class user_orders(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class create_order(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_pk = self.request.GET.get('user')
        user = User.objects.get(pk=user_pk)
        user_address = Profile.objects.filter(user=user).first()

        cart = Cart.objects.get(user=user)
        cart_items = CartItem.objects.filter(cart=cart)

        order = Order.objects.create(user=user, shipping_address=user_address)
        order.save()

        for item in cart_items:
            OrderItem.objects.create(
                order=order, product=item.product, quantity=item.quantity, price=item.product.price)
            product = item.product
            product.quantity -= item.quantity
            product.save()

        cart_items.delete()

        serializer = OrderSerializer(
            order, data={'user': user.pk, 'order_items': [], **request.data})
        if serializer.is_valid():
            serializer.save()
            return redirect('http://localhost:3000/orders')
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class order_details(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        order = Order.get_order_by_user(self, request.user, pk)
        if type(order) == Response:
            return order
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class cancel_order(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        order = Order.get_order_by_id(self, pk)
        if type(order) == Response:
            return order
        if order.user != request.user:
            return Response({'error': 'You are not allowed to cancel this order'}, status=status.HTTP_403_FORBIDDEN)
        if order.created_at + timedelta(days=2) < timezone.now() and order.status != 'delivered':
            return Response({'error': 'Free cancelation time exceeded, you are not allowed to cancel this order'}, status=status.HTTP_403_FORBIDDEN)
        order.status = 'canceled'
        order.save()
        return Response({'message': 'Order cancelled successfully'}, status=status.HTTP_200_OK)