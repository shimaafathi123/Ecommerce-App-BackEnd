
from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from product.models import Product
from user.models import Address

User = get_user_model()

class Order(models.Model):
    STATUS_CHOICES = (
        ("pending", "pending"),
        ("shipped", "shipped"),
        ("delivered", "delivered"),
        ("canceled", "canceled")
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}__{self.id}__{self.total_price}"

    @classmethod
    def get_order_by_id(cls, pk):
        try:
            return cls.objects.get(id=pk)
        except cls.DoesNotExist:
            return Response({'error': 'order does not exist!!'}, status=status.HTTP_404_NOT_FOUND)

    def get_order_by_user(self, user, pk):
        order = self.get_order_by_id(pk)
        if isinstance(order, Order) and order.user != user:
            return Response({'error': 'you are not allowed to view this order'}, status=status.HTTP_403_FORBIDDEN)
        return order

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    #product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name}__{self.quantity}"

    def get_item_price(self):
        return self.quantity * self.product.price

    def save(self, *args, **kwargs):
        self.price = self.get_item_price()
        super().save(*args, **kwargs)
        self.order.total_price += self.price
        self.order.save()
