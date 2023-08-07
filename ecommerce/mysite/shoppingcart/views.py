from django.shortcuts import render

# Create your views here.
def display_cart(request):
    cart_items = request.session['cart_items']
    return render(request, 'shoppingcart.html', {'all_items':cart_items})