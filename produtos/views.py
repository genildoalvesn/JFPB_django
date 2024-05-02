from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def ver_produto(request):
    return HttpResponse("Meu primeiro site com django")
