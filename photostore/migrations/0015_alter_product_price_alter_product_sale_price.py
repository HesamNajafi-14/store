# Generated by Django 5.0.6 on 2024-05-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photostore', '0014_alter_product_price_alter_product_sale_price_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15),
        ),
    ]