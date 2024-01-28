from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = ('product_name', 'last_modofied', 'stock',
                           'price', 'is_available', 'category')

    prepopulated_fields = {'slug': ('product_name',)}


admin.site.register(Product, ProductAdmin)
