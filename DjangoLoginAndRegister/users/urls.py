from django.urls import path
from .views import *
urlpatterns = [
    path("", main_page, name="main"),
    path("login/",login_page, name="login_page"),
    path("register/",register_page,name="register_page"),
    path("logout/",log_out,name = "logout"),
    path("main_panel/",main_panel,name="main_panel"),
    path("detail/<int:id>/",detail,name="detail"),
    path("order/<int:product_id>/",order,name="order"),
]
