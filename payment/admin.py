from django.contrib import admin
from .models import ShippingAddress
from django.contrib.auth.models import User


# Register the model on the admin section thing
admin.site.register(ShippingAddress)
