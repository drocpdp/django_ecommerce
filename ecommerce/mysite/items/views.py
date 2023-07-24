from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the items index.")

def item_request(request, item_id=-1):
    return HttpResponse("<h3>items view, item</h3><h1>{}</h1>".format(str(item_id)))
