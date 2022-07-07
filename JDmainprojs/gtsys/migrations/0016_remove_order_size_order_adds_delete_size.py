# Generated by Django 4.0.3 on 2022-07-04 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gtsys', '0015_addons_rename_tag_size_remove_product_size_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='size',
        ),
        migrations.AddField(
            model_name='order',
            name='adds',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gtsys.addons'),
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
