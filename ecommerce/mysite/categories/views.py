from django.shortcuts import render
from django.http import HttpResponse

def categories(request):
    return HttpResponse("Hello, world. You're at the categories index.")
