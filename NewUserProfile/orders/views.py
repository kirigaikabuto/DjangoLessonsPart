from django.shortcuts import render

# Create your views here.
def order(request):
    product_id = request.POST['product_id']
    quantuty = request.POST['quantity']
    product = Product.objects.get(pk=product_id)
    if product.quantity<quantuty:
        return HttpRessponse("Унас нет такого колво")