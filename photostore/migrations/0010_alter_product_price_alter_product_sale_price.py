# Generated by Django 5.0.6 on 2024-05-16 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photostore', '0009_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.SmallIntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.SmallIntegerField(blank=True, default='', max_length=20),
        ),
    ]