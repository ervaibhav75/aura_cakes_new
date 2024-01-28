from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    cat_slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    cat_img = models.ImageField(upload_to='photoes/categories', blank=True)

    def __str__(self):
        return self.category_name

    def get_url(self):
        return reverse('product_by_category', args=[self.cat_slug])

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
