from django.shortcuts import render, get_object_or_404
from .models import Product

from carts.views import _cart_id
from category.models import Category

from carts.models import CartItem
# Create your views here.


def store(request, category_slug=None):
    category = None
    product = None

    if category_slug:
        category = get_object_or_404(Category, cat_slug=category_slug)
        product_list = Product.objects.all().filter(
            category=category, is_available=True)
    else:
        product_list = Product.objects.all().filter(is_available=True)

    context = {
        'product_list': product_list,
        'product_count': len(product_list)
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):

    try:
        item = Product.objects.get(
            category__cat_slug=category_slug, slug=product_slug)

        in_cart = CartItem.objects.filter(
            cart_id__cart_id=_cart_id(request), product=item.id).exists()

    except Exception as e:
        raise e

    context = {'item': item, 'added_to_cart': in_cart}
    return render(request, 'store/product_detail.html', context)
