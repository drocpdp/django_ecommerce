from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from mysite.items.models import ItemForSale

def index(request):
    return HttpResponse("Hello, world. You're at the items index.")

def item_request(request, item_id=-1):
    return HttpResponse("items view, item <h1>{}</h1>".format(str(item_id)))

def add_item_to_cart(request, item_uuid=-1):
    post_obj = get_object_or_404(ItemForSale, item_uuid=item_uuid)

    # item just added
    cart_item = {
        'item_uuid': post_obj.item_uuid,
        'item_name': post_obj.item_name,
        'item_description': post_obj.item_description,
        'item_price': str(post_obj.item_price)
    }

    if 'cart_items' not in request.session:
        request.session['cart_items'] = [cart_item]
    else:
        old_items = request.session['cart_items']
        old_items.append(cart_item)
        request.session['cart_items'] = old_items #now new items
    
    cart_items = request.session['cart_items']
    
    return render(request, 'shoppingcart.html', {'all_items':cart_items})


def clear_cart(request):
    if 'cart_items' in request.session:
        del request.session['cart_items']
    
    return render(request, 'clearedcart.html')