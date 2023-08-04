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

    cart_item = {
        'item_uuid': post_obj.item_uuid,
        'item_name': post_obj.item_name,
        'item_description': post_obj.item_description,
        'item_price': str(post_obj.item_price)
    }

    if 'cart_items' not in request.session:
        request.session['cart_items'] = [cart_item]
    else:
        cart_items = request.session['cart_items']
        cart_items.append(cart_item)
        request.session['cart_items'] = cart_items
    
    print(request.session.items())
    return HttpResponse("Items added to cart. ID=" + 
                        ", " + str(post_obj.item_name) + 
                        ", " + str(post_obj.item_description) + 
                        ", " + str(post_obj.item_price) + 
                        ", " + str(post_obj.item_uuid) + '<br><a href="/">Back to Home</a>' + '<br><a href="/items/clear_cart/">Clear Cart</a>')

def clear_cart(request):
    if 'cart_items' in request.session:
        del request.session['cart_items']
    
    return HttpResponse("Cart has been cleared. <a href='/'>Back to home</a>")