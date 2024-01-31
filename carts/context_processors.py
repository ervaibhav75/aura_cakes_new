from .views import _cart_id
from .models import Cart, CartItem

# comeback 1


def cart_items_count(request):
    total_items = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart_number = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart_id=cart_number)
            for single_item in cart_items:
                total_items += single_item.quantity
        except Cart.DoesNotExist:
            total_items = 0

    return dict(total_cart_items=total_items)
