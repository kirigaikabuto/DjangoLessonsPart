from django.urls import path
from .views import *


urlpatterns = [
    path('', main_page, name="home"),
    path('register/', register_page, name="register_page"),
]
