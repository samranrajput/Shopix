from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)

class BannerImageInline(admin.TabularInline):
    model = Banner
    extra = 1

class WebNameAdmin(admin.ModelAdmin):
    inlines = [BannerImageInline]

admin.site.register(WebSetting, WebNameAdmin)