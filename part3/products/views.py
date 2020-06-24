from django.shortcuts import render


def list_products(request):
    return render(request, "products/list_page.html")


def detail(request,name):
    return render(request,"products/detail_page.html")