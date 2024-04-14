from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Product, Category
from django.core.exceptions import ValidationError

class ProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_valid_product(self):
        product = Product(
            name='Test Product',
            description='Test Description',
            image=SimpleUploadedFile('test_image.jpg', b''),
            price=10.00,
            rating=4.5,
            quantity=100,
            category=self.category
        )
        product.full_clean()  

    def test_negative_price(self):
        with self.assertRaises(ValidationError):
            product = Product(
                name='Test Product',
                description='Test Description',
                image=SimpleUploadedFile('test_image.jpg', b''),
                price=10.00,  
                rating=4.5,
                quantity=100,
                category=self.category
            )
            product.full_clean()


