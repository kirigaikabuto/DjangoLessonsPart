from django.http import HttpResponse


def main_page(request):
    print("it is main page")
    return HttpResponse("it is main page")


def contacts_page(request):
    print("it is contact page")
    return HttpResponse("it is contact page")


def about_us_page(request):
    print("it is about us page")
    return HttpResponse("it is about us page")




