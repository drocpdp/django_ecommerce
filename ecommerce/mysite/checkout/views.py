from django.shortcuts import render
from django.http import HttpResponse

def checkout(request):
    return HttpResponse("Hello, world. You're at the checkout index.")

def add_to_cart(request, item_name=None):
    return HttpResponse("add_to_cart()")