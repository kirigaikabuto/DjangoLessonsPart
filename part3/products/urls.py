from django.urls import path
from .views import *

urlpatterns = [
    path("all/", list_products, name="all"),
    path("detail/<str:name>/", detail, name="detail"),
]
