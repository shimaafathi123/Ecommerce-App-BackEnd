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

    
    def get_object(self):
        # Get the cart of the logged-in user
        return self.request.user.cart

# class CartDetailView(generics.RetrieveAPIView):
#     serializer_class = CartSerializer
#     permission_classes = [IsAuthenticated]


#     #   queryset = Cart.objects.all()
#     # lookup_field = 'pk'
# # class CartDetailView(generics.RetrieveAPIView):
# #     serializer_class = CartSerializer
# #     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         return Cart.objects.filter(user=user)

#     lookup_field = 'user__id'

class DeleteCartItemView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()

    def delete(self, request, pk, *args, **kwargs):
        try:
            instance = self.get_object()
            Product = instance.product
            Product.quantity += instance.quantity
            Product.save()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart Item doesn't exist"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
