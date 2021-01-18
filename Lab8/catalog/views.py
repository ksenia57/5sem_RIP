from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
    )

from django.views import generic

def film1(request):
    return render(
        request,
        'Parazit.html'
    )

def film2(request):
    return render(
        request,
        'Busan.html'
    )

def film3(request):
    return render(
        request,
        'Busan2.html'
    )