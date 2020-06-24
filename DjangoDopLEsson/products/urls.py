
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("all/",list_page,name="list")
]
