from django.urls import path
from .views import *
urlpatterns = [
    path("all/",list_products),
    path("detail/<str:name>/",detail),
]
# http://127.0.0.1:8000/products/detail/sdsdsd/