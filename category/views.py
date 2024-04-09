from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from product.models import Product  
from .serializers import CategorySerializer
from product.serializers import ProductSerializer

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategoryProductListView(APIView):
    def get(self, request, category_id):
        try:
            products = Product.objects.filter(category_id=category_id)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
