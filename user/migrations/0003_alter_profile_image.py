# Generated by Django 5.0.3 on 2024-04-07 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_profile_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default/default-user.jpg', null=True, upload_to='accounts/users/'),
        ),
    ]
