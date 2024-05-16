from django.db import models
import datetime




class Category(models.Model):
	name = models.CharField(max_length=50)
	

	def __str__(self):
		return self.name


class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=11)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=30)

	def __str__(self):
		return f'{self.first_name} - {self.last_name}'


class Product(models.Model):
	name = models.CharField(max_length=50)
	price = models.CharField(max_length=20)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	describtion = models.TextField(max_length=250, default='')
	image = models.ImageField(upload_to='upload/photo/')
	is_sale = models.BooleanField(default=False)
	sale_price = models.CharField(max_length=20, default='', blank=True)


	def __str__(self):
		return self.name


class Order(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	address = models.CharField(max_length=100, default='')
	phone = models.CharField(max_length=11, default='', blank=True)
	date = models.DateField(default=datetime.datetime.today)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.product



