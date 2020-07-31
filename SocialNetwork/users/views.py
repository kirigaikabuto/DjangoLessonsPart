from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import *


def register_page(request):
    user_form = None
    profile_form = None
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileCreationForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():

            my_user = user_form.save()
            # возвращет модели коротую использует
            profile = profile_form.save(commit=False)

            profile.user = my_user

            profile.save()
            return HttpResponse("user is created")
    user_form = UserCreationForm()
    profile_form = ProfileCreationForm()

    myuser = User.objects.get(username="kirito871717")
    profile = Profile.objects.get(user=myuser)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "profile": profile
    }
    return render(request, "users/register.html", context=context)

