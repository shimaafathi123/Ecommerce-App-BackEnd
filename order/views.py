from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
from django.shortcuts import redirect
from django.conf import settings
from django.utils import timezone
from rest_framework import status


class userOrder(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class cancel_order(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            order = Order.objects.get(pk=pk, user=request.user)
        except Order.DoesNotExist:
            return Response({'error': 'Order does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if order.status == 'delivered':
            return Response({'error': 'You cannot cancel a delivered order'}, status=status.HTTP_403_FORBIDDEN)

        cancelation_time_limit = timezone.now() - timezone.timedelta(days=2)
        if order.created_at < cancelation_time_limit:
            return Response({'error': 'the cancelation time exceed'}, status=status.HTTP_403_FORBIDDEN)

        order.status = 'canceled'
        order.save()
        return Response({'message': 'Order canceled successfully'}, status=status.HTTP_200_OK)

class order_details(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        order = Order.objects.filter(user=request.user, pk=pk).first()
        if not order:
            return Response({'error': 'Order does not exist !'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order)
        return Response(serializer.data)


# Create your views here.
