from rest_framework import generics, status
from rest_framework.response import Response
from shopping_cart.models import Cart, CartItem
from shopping_cart.serializers import AddToCartSerializer, UpdateCartSerializer, CartSerializer
from rest_framework.permissions import IsAuthenticated
from product.models import Product


class AddToCartView(generics.CreateAPIView):
    serializer_class = AddToCartSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateCartItemView(generics.UpdateAPIView):
    serializer_class = UpdateCartSerializer
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, *args, **kwargs):
        action = request.data.get('action')
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(action=action)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user'

    def get_queryset(self):
        user_id = self.request.user.id
        return Cart.objects.filter(user=user_id)


class DeleteCartItemView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()

    def delete(self, request, pk, *args, **kwargs):
        try:
            instance = self.get_object()
            product = instance.product
            product.quantity += instance.quantity
            product.save()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart Item doesn't exist"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
