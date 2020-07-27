from django.shortcuts import render,HttpResponse
from .models import *


def order(request):
    product_id = request.POST['product_id']
    quantity = request.POST['quantity']
    product = Product.objects.get(pk=product_id)
    if product.quantity<quantity:
        return HttpResponse("Унас нет такого колво")