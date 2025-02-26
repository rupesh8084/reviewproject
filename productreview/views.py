from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Product

def product_list(request):
    products=Product.objects.all()
    return render(request, 'product_list.html', {'products':products})

