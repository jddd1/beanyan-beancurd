# Generated by Django 4.0.3 on 2022-07-05 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtsys', '0017_remove_order_adds_alter_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(max_length=200, null=True)),
                ('customeremail', models.CharField(max_length=200, null=True)),
                ('customerphone', models.CharField(max_length=200, null=True)),
                ('customeraddress', models.CharField(max_length=200, null=True)),
                ('customerconcern', models.CharField(choices=[('Product Complaints', 'Product Complaints'), ('Question', 'Question'), ('Delivery Issues', 'Delivery Issues'), ('Others', 'Others')], max_length=200, null=True)),
                ('customermessage', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
