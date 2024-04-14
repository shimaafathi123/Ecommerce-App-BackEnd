from django.db import models
from django.forms import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Add unique constraint
    description = models.TextField(blank=True)

    def clean(self):
     
        if not self.name:
            raise ValidationError("Category name cannot be empty.")

    def __str__(self):
        return self.name
