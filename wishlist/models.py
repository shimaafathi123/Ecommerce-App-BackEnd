from django.db import models
from django.db import models
from user.models import User
from product.models import Product


class Wishlist(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)
    products = models.ManyToManyField(Product, related_name='wish_list', through='Wishlist_Item') 
    def __str__(self):
        return f'wishlist for {self.user.username}'
        
class Wishlist_Item(models.Model):
    product = models.ForeignKey( Product, on_delete=models.CASCADE, related_name="wishlist_items")
    wish_list = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name="favs")
    def __str__(self):
        return self.product.name






