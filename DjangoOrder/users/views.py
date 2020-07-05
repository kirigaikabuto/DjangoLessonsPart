from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def order_product(request,id):
    product = Product.objects.get(pk=id)
    user = request.user
    order = Order(user=user,product=product)
    order.save()
    return redirect("main_panel")