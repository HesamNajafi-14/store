# Generated by Django 5.0.6 on 2024-05-15 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photostore', '0008_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=20),
        ),
    ]
