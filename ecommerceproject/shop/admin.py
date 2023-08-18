from django.contrib import admin
from . models import Category,Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_name','slug']
    prepopulated_fields = {'slug':('cat_name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['pro_name','price','category','stock','available','created','updated']
    prepopulated_fields = {'slug':('pro_name',)}
    list_editable = ['price','available','stock']
    list_per_page = 20
admin.site.register(Product,ProductAdmin)

