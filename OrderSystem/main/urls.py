from django.urls import path
from .views import *


urlpatterns = [
    path('', main_page, name="home_page"),
    path('register/', register_page, name="register_page"),
    path('login/', login_page, name="login_page"),
    path('logout/', log_out, name="logout"),
    path('order/<int:id_product>/', do_order, name='do_order')
]
