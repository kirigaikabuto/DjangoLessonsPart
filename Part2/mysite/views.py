from django.http import HttpResponse
from django.shortcuts import render


def main_page(request):
    a = "Hello it python"
    array = [1, 2, 3, 4, 5]
    d = {
        "message": a,
        "array": array,
        "name" : "Yerassyl",
    }
    return render(request, "main/main_page.html", context=d)


def contacts_page(request):
    print("it is contact page")
    return render(request,"main/contacts_page.html")


def about_us_page(request):
    print("it is about us page")
    return HttpResponse("it is about us page")




