"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from mysite import homepage

urlpatterns = [
    path('', include('mysite.homepage.urls')),    
    path('admin/', admin.site.urls),
    path('categories/', include('mysite.categories.urls')),
    path('checkout/', include('mysite.checkout.urls')),
    path('items/', include('mysite.items.urls')),
    path('item_detail/', include('mysite.item_detail.urls')),
    path('shoppingcart/', include('mysite.shoppingcart.urls'))
]
