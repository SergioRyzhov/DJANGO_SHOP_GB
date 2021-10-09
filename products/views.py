from django.shortcuts import render
import json

# Create your views here.


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)

def products(request):
    with open('geekshop/products/fixtures/products.json',"r", encoding="utf-8") as f:
        context = json.load(f)
    return render(request, 'products/products.html', context)