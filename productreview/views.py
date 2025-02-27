from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Product
from .models import Review

def product_list(request):
    products=Product.objects.all()
    return render(request, 'product_list.html', {'products':products})

def review_list(request):
    reviews=Review.objects.all()
    return render(request, 'review_list.html', {'reviews':reviews})