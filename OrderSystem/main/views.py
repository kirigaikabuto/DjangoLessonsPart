from django.shortcuts import render
from django.contrib.auth.models import User


def main_page(request):
    return render(request, "main/home.html")


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
