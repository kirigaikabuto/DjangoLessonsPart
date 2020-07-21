from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from products.models import *
from orders.models import *


def do_order(request, id_product):
    userObject = request.user
    product = Product.objects.get(pk=id_product)
    order = Order(user=userObject, product=product)
    order.save()
    return redirect("home_page")


def log_out(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    error = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if len(username) == 0 or len(password) == 0:
            error = "Заполните все поля"
        else:
            userObject = authenticate(request, username=username, password=password)
            if userObject is None:
                error = "нет такого пользователя"
            else:
                login(request, userObject)
                return redirect("home_page")
    d = {
        "error": error
    }
    return render(request, "main/login.html", context=d)


def main_page(request):
    products = Product.objects.all()
    d = {
        "products":products,
    }
    return render(request, "main/home.html", context=d)


def register_page(request):
    error = ""
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        if len(first_name) == 0:
            error = "Заполните имя"
        elif len(last_name) == 0:
            error = "Заполните фамилиюю"
        else:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            user.save()

    d = {
        "error": error
    }

    return render(request, "main/register.html", context=d)
