from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        
        if category_id:
            queryset = Product.objects.filter(category_id=category_id)
        else:
            queryset = Product.objects.all()
        
        return queryset

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class RelatedProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_id = self.kwargs.get('pk')
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            related_products = product.related_products()
            return related_products
