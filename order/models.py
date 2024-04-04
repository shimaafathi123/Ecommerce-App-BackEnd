from django.db import models

class Order(models.Model):
    STATUS_CHOICES = (
        ("pending", "pending"),
        ("shipped", "shipped"),
        ("delivered", "delivered"),
        ("canceled", "canceled")
    )

# Create your models here.
