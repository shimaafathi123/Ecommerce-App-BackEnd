from .models import Order, OrderItem, User
from shopping_cart.models import Cart, Cart_Item
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

stripe.api_key = settings.STRIPE_SECRET_KEY


class user_order(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class check_out(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart does not exist'}, status=status.HTTP_404_NOT_FOUND)

        cart_items = Cart_Item.objects.filter(cart=cart)

        if not cart_items:
            return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

        for item in cart_items:
            if item.quantity > item.product.quantity:
                return Response({'error': f'Product {item.product.name} is out of stock'}, status=status.HTTP_400_BAD_REQUEST)

        line_items = []
        for item in cart_items:
            product_name = item.product.name
            price = int(item.product.price * 100)
            line_item = {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product_name,
                    },
                    'unit_amount': price
                },
                'quantity': item.quantity
            }
            line_items.append(line_item)
        try:
            base_url = request.scheme + '://' + request.get_host()
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items, 
                mode='payment',
                success_url=f'{base_url}/orders/create/?user={request.user.pk}',
                cancel_url=f'{base_url}/users/cart/',
            )

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'url': checkout_session.url})


class create_order(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_pk = self.request.GET.get('user')
        user = User.objects.get(pk=user_pk)
        user_address = Address.objects.filter(user=user).first()

        cart = Cart.objects.get(user=user)
        cart_items = Cart_Item.objects.filter(cart=cart)

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

class order_details(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        order = Order.objects.filter(user=request.user, pk=pk).first()
        if not order:
            return Response({'error': 'order does not exist !!'}, status=status.HTTP_404_NOT_FOUND)

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
    
