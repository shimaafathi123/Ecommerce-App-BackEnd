from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Wishlist, Wishlist_Item
from .serializers import WishListSerializer, EditWishlistItemSerializer
import jwt
from .models import User,Product
# Create your views here.
class user_wishlist(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WishListSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        print(user_id)
        return Wishlist.objects.filter(user=user_id)


class create_item(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EditWishlistItemSerializer

    def post(self, request, product, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={
                                         "user": request.user, "product_id": product})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WishlistItem(generics.CreateAPIView, generics.RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = EditWishlistItemSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        wishlist = Wishlist.objects.filter(user=user_id).first()
        items = Wishlist_Item.objects.filter(wish_list=wishlist)
        return items

    def post(self, request, pk, *args, **kwargs):
        Myjwt = request.data['headers']['Authorization'].split()[1]
        payload = jwt.decode(Myjwt, 'django-insecure-sl$tdf82tnh*#!clf(0wgf$fr_!cw^l!yx-sig8y%ev*q9r7k+')
        user_id = int(payload['user_id'])

        try:
            user = User.objects.get(id=user_id)
            wishlist, created = Wishlist.objects.get_or_create(user=user)

            product_id = int(pk)
            product = Product.objects.get(id=product_id)

            wishlist_item, created = Wishlist_Item.objects.get_or_create(
                wish_list=wishlist, product=product)

            serializer = self.get_serializer(wishlist_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Product.DoesNotExist:
            return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
    def destroy(self, request, pk, *args, **kwargs):
        print(self.get_queryset().values())
        try:
            instance = self.get_queryset().get(product_id=pk)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Wishlist_Item.DoesNotExist:
            return Response({"error": "WishList Item doesn't exist"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
