from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


@csrf_exempt
def ver_produto(request):
    return HttpResponse("Meu primeiro site com django")
