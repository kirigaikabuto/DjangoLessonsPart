from django.shortcuts import render
from .models import *


def list_products(request):

    return render(request, "products/list_page.html")


def detail(request, name):
    product = Product.objects.get(name=name)
    d = {
        "product" : product,
    }
    return render(request, "products/detail_page.html", context=d)
