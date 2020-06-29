from django.shortcuts import render
from books.models import *

#obje
def index(request):
    if request.method == "POST":
        value = request.POST['search_value']
        books = Book.objects.all().filter(name=value)
    else:
        books = Book.objects.all()

    d = {
        "books": books,
    }
    return render(request,"main/index.html", context=d)