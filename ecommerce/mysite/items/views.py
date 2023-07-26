from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from mysite.items.models import ItemForSale

def index(request):
    return HttpResponse("Hello, world. You're at the items index.")

def item_request(request, item_id=-1):
    return HttpResponse("items view, item <h1>{}</h1>".format(str(item_id)))

def add_item_to_cart(request, item_uuid=-1):
    print(request)
    post_obj = get_object_or_404(ItemForSale, item_uuid=item_uuid)
    print(post_obj.item_name, post_obj.item_description, post_obj.item_price)
    return HttpResponse("Items added to cart. ID=" + 
                        ", " + str(post_obj.item_name) + 
                        ", " + str(post_obj.item_description) + 
                        ", " + str(post_obj.item_price))
