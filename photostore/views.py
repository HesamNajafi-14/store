from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignUpForm

def category(request, foo):
	foo = foo.replace('-', ' ')
	try:
		category = Category.objects.get(name=foo)
		products = Product.objects.filter(category=category)
		return render(request, 'category.html', {'products':products, 'category':category})
	except:
		messages.success(request, ("That Category Does not Exist..."))
		return redirect('home')


def photoPage(request, pk):
	photo = Product.objects.get(id=pk)
	return render(request, 'photodetails.html', {'photo':photo})


class HomePageView(ListView):
	template_name = 'home.html'
	model = Product
	paginate_by = 4

	

class AboutPageView(TemplateView):
	template_name = 'about.html'


def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ("You Logged In Successfully..."))
			return redirect('home')
		else:
			messages.success(request, ("There was an error please try again..."))
			return redirect('login')
	else:
		return render(request, 'login.html', {})


def logout_user(request):
	logout(request)
	messages.success(request, ("You Logged Out...Please ComeBack Soon"))
	return redirect('home')

def register_user(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("You Registered Successfully..."))
			return redirect('home')
		else:
			messages.success(request, ("There was a problem ... please try it again..."))
			return redirect('register')

	return render(request, 'register.html', {'form':form})
