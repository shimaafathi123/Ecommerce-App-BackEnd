from django.db import models
from django.forms import ValidationError
from category.models import Category

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='product_images/', verbose_name='Image')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', help_text='Enter price in format X.XX')
    rating = models.FloatField(verbose_name='Rating', help_text='Enter rating between 0 and 5')
    quantity = models.PositiveIntegerField(verbose_name='Quantity', help_text='Enter available quantity')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')

    def clean(self):
        if self.price < 0:
            raise ValidationError("Price cannot be negative.")
        if not 0 <= self.rating <= 5:
            raise ValidationError("Rating must be between 0 and 5.")
        if self.quantity < 0:
            raise ValidationError("Quantity cannot be negative.")
            
    def related_products(self):
        return Product.objects.filter(category_id=self.category_id).exclude(id=self.id)[:5]  

    def __str__(self):
        return self.name
