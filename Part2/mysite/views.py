from django.http import HttpResponse
from django.shortcuts import render


def main_page(request):
    print("it is main page")
    return render(request, "main/main_page.html")


def contacts_page(request):
    print("it is contact page")
    return render(request,"main/contacts_page.html")


def about_us_page(request):
    print("it is about us page")
    return HttpResponse("it is about us page")




