from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def main_page(request):
    return render(request, "users/main.html")


def login_page(request):
    error = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if len(username) == 0 and len(password) == 0:
            error = "Заполните все поля"
        elif len(username) == 0:
            error = "Заполните username"
        elif len(password) == 0:
            error = "Заполните password"
        else:
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is None:
                error = "нет такого пользователя"
            else:
                login(request, user)
                return redirect("main")
    d = {
        "error": error
    }
    return render(request, "users/login.html", context=d)


def register_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        u = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        u.save()
        return redirect("main")
    return render(request, "users/register.html")


def log_out(request):
    logout(request)
    return redirect("main")
