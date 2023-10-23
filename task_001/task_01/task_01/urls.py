from django.urls import path
from task01app import views

urlpatterns = [
    path('coin_flip/', views.coin_flip, name='coin_flip'),
    path('roll_dice/', views.roll_dice, name='roll_dice'),
    path('random_number/', views.random_number, name='random_number'),
]
