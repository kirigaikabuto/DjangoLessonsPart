from django.urls import path, include
from .views import *


urlpatterns = [
   path("", home_page, name="home_page"),
]