from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)

def products(request):
    context = {
            'title': 'GeekShop - Каталог',
                'products': [
                    {'name': 'Худи черного цвета с монограммами adidas Originals',
                    'img': 'vendor/img/products/Adidas-hoodie.png',
                    'price': '6090',
                    'desc': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                    'button': '<button type="button" class="btn btn-outline-success">Отправить в корзину</button>'},

                    {'name': 'Синяя куртка The North Face',
                    'img': 'vendor/img/products/Blue-jacket-The-North-Face.png',
                    'price': '23725',
                    'desc': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                    'button': '<button type="button" class="btn btn-outline-danger">Удалить из корзины</button>'},

                    {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                    'img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                    'price': '3390',
                    'desc': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                    'button': '<button type="button" class="btn btn-outline-success">Отправить в корзину</button>'},

                    {'name': 'Черный рюкзак Nike Heritage',
                    'img': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
                    'price': '2340',
                    'desc': 'Плотная ткань. Легкий материал.',
                    'button': '<button type="button" class="btn btn-outline-success">Отправить в корзину</button>'},

                    {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                    'img': 'vendor/img/products/Black-Dr-Martens-shoes.png',
                    'price': '13590',
                    'desc': 'Гладкий кожаный верх. Натуральный материал.',
                    'button': '<button type="button" class="btn btn-outline-success">Отправить в корзину</button>'},

                    {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                    'img': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                    'price': '2890',
                    'desc': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                    'button': '<button type="button" class="btn btn-outline-success">Отправить в корзину</button>'},
                ]
            }
    return render(request, 'products/products.html', context)