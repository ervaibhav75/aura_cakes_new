from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse
from carts.views import _cart_id
from category.models import Category
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from carts.models import CartItem
# Create your views here.


def store(request, category_slug=None):
    category = None
    product = None
    page = request.GET.get('page')

    if category_slug:
        category = get_object_or_404(
            Category, cat_slug=category_slug)
        product_list = Product.objects.all().filter(
            category=category, is_available=True).order_by('id')
        Paginator_Object = Paginator(product_list, 4)
        paged_products = Paginator_Object.get_page(page)

    else:
        product_list = Product.objects.all().filter(is_available=True).order_by('id')
        Paginator_Object = Paginator(product_list, 6)
        paged_products = Paginator_Object.get_page(page)

    context = {
        'product_list': paged_products,
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


def search(request):
    context = {}
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            if not products:
                print('not found')

            context['product_list'] = products
            context['product_count']= len(products)

    return render(request, 'store/store.html', context)
