# Generated by Django 5.0.6 on 2024-05-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photostore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=20),
        ),
    ]