# Generated by Django 4.0.3 on 2022-07-06 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtsys', '0020_rename_main_name_cart_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='adds_name',
        ),
    ]
