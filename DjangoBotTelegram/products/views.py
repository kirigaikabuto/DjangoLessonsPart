from django.shortcuts import render, HttpResponse


def products_all(request):
    d = {
        "product_name": "product1",
        "price": 400,
    }
    return render(request, "products/all.html", context=d)
    # return HttpResponse("it is page for all products")


def product_detail(request):
    return render(request, "products/detail.html")
    # return HttpResponse("it is page for product detail")