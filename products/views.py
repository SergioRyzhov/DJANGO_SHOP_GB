from django.shortcuts import render
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
    "products": [
        {"img": "products_images/Adidas-hoodie.png",
        "price": "6090",
        "desc": "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.",
        "button": "<button type='button' class='btn btn-outline-success'>Отправить в корзину</button>"
        },
        {"img": "products_images/Blue-jacket-The-North-Face.png",
        "price": "23725",
        "desc": "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.",
        "button": "<button type='button' class='btn btn-outline-danger'>Удалить из корзины</button>"
        },
        {"img": "products_images/Brown-sports-oversized-top-ASOS-DESIGN.png",
        "price": "3390",
        "desc": "Материал с плюшевой текстурой. Удобный и мягкий.",
        "button": "<button type='button' class='btn btn-outline-success'>Отправить в корзину</button>"
        },
        {"img": "products_images/Black-Nike-Heritage-backpack.png",
        "price": "2340",
        "desc": "Плотная ткань. Легкий материал.",
        "button": "<button type='button' class='btn btn-outline-success'>Отправить в корзину</button>"
        },
        {"img": "products_images/Black-Dr-Martens-shoes.png",
        "price": "13590",
        "desc": "Гладкий кожаный верх. Натуральный материал.",
        "button": "<button type='button' class='btn btn-outline-success'>Отправить в корзину</button>"
        },
        {"img": "products_images/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png",
        "price": "2890",
        "desc": "Легкая эластичная ткань сирсакер Фактурная ткань.",
        "button": "<button type='button' class='btn btn-outline-success'>Отправить в корзину</button>"
        }
    ]}
    for i in range(len(j_context['products'])):
        context['products'][i]['name'] = j_context['products'][i]['name']
    return render(request, 'products/products.html', context)