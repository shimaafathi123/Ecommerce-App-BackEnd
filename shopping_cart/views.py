from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from shopping_cart.models import CartItem, Cart
from .serializers import CartSerializer, AddToCartSerializer, UpdateCartSerializer
from rest_framework.permissions import IsAuthenticated
from product.models import Product


class CartDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get_object(self):
        user_id = self.request.user.id
        cart = Cart.objects.filter(user=user_id).first()
        return cart


class CartItemCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddToCartSerializer

    def post(self, request, product_id, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={
         "user": request.user, "product_id": product_id})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateCartSerializer
    queryset = CartItem.objects.all()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
