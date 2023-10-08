from django.http import HttpResponse
import logging

# Получаем логгер
logger = logging.getLogger(__name__)

def index(request):
    html = """
    <html>
        <head>
            <title>Главная страница</title>
        </head>
        <body>
            <h1>Добро пожаловать на мою главную страницу!</h1>
            <p>Здесь вы найдете информацию о моем Django-сайте.</p>
        </body>
    </html>
    """
    # Сохраняем информацию о посещении в логи
    logger.info("The user visited the main page")
    return HttpResponse(html)

def about(request):
    html = """
    <html>
        <head>
            <title>О себе</title>
        </head>
        <body>
            <h1>Обо мне</h1>
            <p>Я - разработчик Django. Это моя страница "о себе".</p>
        </body>
    </html>
    """
    # Сохраняем информацию о посещении в логи
    logger.info("The user visited the 'About' page")
    return HttpResponse(html)

