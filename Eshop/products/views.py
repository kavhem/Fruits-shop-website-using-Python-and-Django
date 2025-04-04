from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})


def new(request):
    return HttpResponse("new products")


def vivo20(request):
    return HttpResponse("vivo V20")

def hemanth(request):
    return HttpResponse("HI HEMANTH GOWDA K R")

