from django.db import models
from user.models import User
from product.models import Product

class Wishlist(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    products = models.ManyToManyField(Product)
    
    def __str__(self):
        return f"Wishlist for {self.user.username}"
