# Generated by Django 5.0.3 on 2024-04-19 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_alter_order_delivered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 22, 22, 6, 46, 45864, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]