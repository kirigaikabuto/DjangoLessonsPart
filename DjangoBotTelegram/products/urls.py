from django.urls import path
from .views import *

urlpatterns = [
    path("all/", products_all),
    path("detail/", product_detail)
]
