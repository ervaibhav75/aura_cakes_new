
from django.db import models
from django.urls import reverse
from category.models import Category
# Create your models here.


def is_product_added(self, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_object = Cart.objects.get(cart_id=_cart_id(self.request))
    cart_item_object = CartItem.objects.get(
        product=product, cart_id=cart_object)

    if cart_item_object:
        return True
    else:
        return False


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photoes/products')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('product_detail', args=[self.category.cat_slug, self.slug])
