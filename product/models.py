from django.db import models

from category.models import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    def related_products(self):
        return Product.objects.filter(category_id=self.category_id).exclude(id=self.id)[:5]  
