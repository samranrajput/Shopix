from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['category_id','category_name','category_logo','description','created_at','updated_at']
#     search_fields = ('category_name',)
#     ordering = ('-created_at',)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['product_id','product_name','product_image','description','category','stock','price','is_available','created_at','updated_at']
#     list_filter = ('category', 'is_available')
#     search_fields = ('product_name', 'category__category_name')
#     ordering = ('-created_at',)