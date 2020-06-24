from django.urls import path
from .views import *

urlpatterns = [
    path("all/", list_products, name="all"),
    path("detail/<str:name>/", detail, name="detail"),
]
# http://127.0.0.1:8000/products/detail/sdsdsd/
# http://127.0.0.1:8000/products/detail/product3/
