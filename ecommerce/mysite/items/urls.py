from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("clear_cart/", views.clear_cart, name="clear_cart"),
    path("<int:item_id>/", views.item_request, name="index"),
    path("additem/<uuid:item_uuid>/", views.add_item_to_cart, name="additem")

]