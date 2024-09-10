from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, "main.html", context)