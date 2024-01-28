from django.shortcuts import HttpResponse, render
from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'product_list': products
    }
    return render(request, "home.html", context)
