from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    base_template = loader.get_template('base.html')
    context = {
        'context1':'This is context one',
        'context2':'This is context two',
        'context3':'This is context three'
    }
    return HttpResponse(base_template.render(context, request))