from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def main_panel(request):
    user = request.user
    profile = Profile.objects.get(user = user)
    d = {
        "profile": profile
    }
    return render(request, "userprofile/main_panel.html", context=d)


def log_out(request):
    logout(request)
    return redirect("login_page")


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
                return redirect("main_panel")
    d = {
        "error": error
    }
    return render(request, "userprofile/login.html", context=d)


def register_page(request):
    error = ""

    if request.method == "POST":
        #get data
        username = request.POST['username']
        password = request.POST['password']
        address = request.POST['address']
        department_id = int(request.POST['department'])

        #create user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        #get department
        department = Department.objects.get(pk=department_id)

        #calculate salary
        percent = 0.0
        if department.name == "IT":
            percent = 0.3
        elif department.name == "Finance":
            percent = 0.2
        salary = (department.max_salary+department.min_salary)/2 + (department.min_salary*percent)

        #create profile
        profile = Profile(user=user, department=department, address=address, salary=salary)
        profile.save()
        return redirect("login_page")
    departments = Department.objects.all()
    d = {
        "error": error,
        "departments": departments
    }
    return render(request, "userprofile/register.html", context=d)