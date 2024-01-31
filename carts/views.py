from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from store.models import Product

# Create your views here.


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def cart(request):
    context = {}
    try:
        cart_objects = Cart.objects.get(cart_id=_cart_id(request))
        all_cart_objects = CartItem.objects.filter(
            cart_id=cart_objects, is_active=True)
        sum = 0
        for item in all_cart_objects:
            sum += item.get_total_price()
        tax = (2 * sum) / 100
        grand_total = sum - tax
        context = {'cart_objects': all_cart_objects,
                   'total_price': sum,
                   'tax': tax,
                   'grand_total': grand_total
                   }

    except Cart.DoesNotExist:
        return render(request, 'store/cart.html', {})
    return render(request, 'store/cart.html', context)


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart_object = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart_object = Cart.objects.create(cart_id=_cart_id(request))
        cart_object.save()
    try:
        cart_item_object = CartItem.objects.get(
            product=product, cart_id=cart_object)
        cart_item_object.quantity += 1
        cart_item_object.save()

    except CartItem.DoesNotExist:
        cart_item_object = CartItem.objects.create(
            product=product, cart_id=cart_object, quantity=1,)

        cart_item_object.save()

    return redirect('cart')


def minus_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_object = Cart.objects.get(cart_id=_cart_id(request))
    cart_item_object = CartItem.objects.get(
        product=product, cart_id=cart_object)
    if cart_item_object.quantity > 1:
        cart_item_object.quantity -= 1
        cart_item_object.save()
    else:
        cart_item_object.delete()
    return redirect('cart')


def delete_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_object = Cart.objects.get(cart_id=_cart_id(request))
    cart_item_object = CartItem.objects.get(
        product=product, cart_id=cart_object)

    cart_item_object.delete()
    return redirect('cart')
