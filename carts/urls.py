
from django.urls import path
from . import views
urlpatterns = [

    path('', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/',
         views.add_to_cart, name='add_to_cart'),
    path('minus_from_cart/<int:product_id>/',
         views.minus_from_cart, name='minus_from_cart'),
    path('delete_from_cart/<int:product_id>/',
         views.delete_from_cart, name='delete_from_cart'),




]
