import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'The "{func.__name__}" function has been launched')
        return result

    return wrapper


# Create your views here.

@log
def main_page(request):
    return HttpResponse('<h1>Главная страница<h1>'
                        '<h5>Тут немного текста<h5>')


@log
def about(request):
    return HttpResponse('<h1>Страница обо мне<h1>'
                        '<h5>Меня зовут Андрей, мне 28 лет<h5>')
