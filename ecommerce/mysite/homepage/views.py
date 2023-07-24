from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models.manager import Manager

from mysite.items.models import ItemForSale, Category

def index(request):
    ui_template = loader.get_template('ui_builder.html')
    all_items = ItemForSale.objects.all()
    items_for_sale = [
        {
            "name": item.item_name,
            "description": item.item_description, 
            "image_url": item.item_image_url,
            "categories": item.item_categories,
            "price": "{:,.2f}".format(item.item_price)
        } for item in all_items
    ]
    print(items_for_sale)
    return render(request, 'ui_builder.html', {'items_for_sale': items_for_sale})