# Generated by Django 5.0.3 on 2024-04-08 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist_items', to='product.product')),
                ('wish_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favs', to='wishlist.wishlist')),
            ],
        ),
        migrations.AddField(
            model_name='wishlist',
            name='products',
            field=models.ManyToManyField(related_name='wish_list', through='wishlist.Wishlist_Item', to='product.product'),
        ),
    ]
