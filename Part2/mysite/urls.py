from django.contrib import admin
from django.urls import path
from .views import *

# base_url = "http://127.0.0.1:8000/"


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main_page),
    path("contacts/", contacts_page),
]
