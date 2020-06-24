from django.shortcuts import render
from .models import *


def list_page(request):
    message = "Hello From list_page view"
    arr = ["good","123","3434"]
    product = Product.objects.get(pk=1)
    products = Product.objects.all()
    # filtered_products = Product.objects.all().filter(price=100)
    # filtered_products = Product.objects.all().filter(price__gte=100)# __gte>=,lte<=  gte->greater
    filtered_products = Product.objects.all().filter(description__contains="good")
    d = {
        "message":message,
        "arr":arr,
        "product":product,
        "products":products,
        "filtered_products":filtered_products,
    }
    return render(request,"products/list.html",context=d)

