# Generated by Django 4.0.3 on 2022-07-03 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtsys', '0003_order_delete_customer_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12, null=True)),
                ('name', models.CharField(max_length=80, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
