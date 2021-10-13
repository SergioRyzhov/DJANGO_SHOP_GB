from django.shortcuts import render
from .models import ProductCategory, Product
import json

# Create your views here.


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)

def products(request):
    with open('geekshop/products/fixtures/products.json',"r", encoding="utf-8") as f:
        j_context = json.load(f)
    context = {
        "title": "GeekShop - Каталог",
        "products": Product.objects.all()
        }
    return render(request, 'products/products.html', context)