# Generated by Django 5.0.6 on 2024-05-14 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photostore', '0006_remove_product_slug_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
