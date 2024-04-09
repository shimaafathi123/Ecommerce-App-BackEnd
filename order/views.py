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