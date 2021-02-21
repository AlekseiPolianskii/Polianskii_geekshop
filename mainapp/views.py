from django.shortcuts import render


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', context)


def prodacts(request):
    context = {
        'title': 'GeekShop - Каталог'
    }
    return render(request, 'mainapp/products.html', context)