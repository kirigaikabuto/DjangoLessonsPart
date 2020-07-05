from django.urls import path
from .views import *
urlpatterns = [
    path("", main_page, name="main"),
    path("login/",login_page, name="login_page"),
    path("register/",register_page,name="register_page"),
    path("logout/",log_out,name = "logout"),
]
