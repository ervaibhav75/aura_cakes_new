from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.


class CartItemsAdmin(admin.ModelAdmin):

    list_display = ('cart_id', 'quantity', 'is_active',
                    )


admin.site.register(Cart)
admin.site.register(CartItem, CartItemsAdmin)
