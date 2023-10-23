from django.http import JsonResponse
from random import randint

def coin_flip(request):
    result = "Heads" if randint(0, 1) == 0 else "Tails"
    return JsonResponse({"result": result})

def roll_dice(request):
    result = randint(1, 6)
    return JsonResponse({"result": result})

def random_number(request):
    result = randint(0, 100)
    return JsonResponse({"result": result})

