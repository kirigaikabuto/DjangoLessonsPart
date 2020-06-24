from django.shortcuts import render
from .models import *


def list_products(request):
    # p1 = Product(name="yerassyl",description="",price=100)
    # p1.save()
    products = Product.objects.all()
    d = {
        "products": products
    }
    return render(request, "products/list_page.html", context=d)


def detail(request, name):
    product = Product.objects.get(name=name)
    d = {
        "product" : product,
    }
    return render(request, "products/detail_page.html", context=d)
