from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    cat_desc = models.TextField(blank=True)
    cat_img = models.ImageField(upload_to='categoryImages', blank=True)

    class Meta:
        ordering = ('cat_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('shop:products_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.cat_name)

class Product(models.Model):
    pro_name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    pro_desc = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pro_img = models.ImageField(upload_to='productImages', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('pro_name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('shop:prodCatdetail',args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.pro_name)
