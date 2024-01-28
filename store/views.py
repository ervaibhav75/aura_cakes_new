from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
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

    except Exception as e:
        raise e

    context = {'item': item, }
    return render(request, 'store/product_detail.html', context)
