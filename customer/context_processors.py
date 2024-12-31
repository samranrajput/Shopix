from administrator.models import *

def base_logic(request):
    categories = Category.objects.prefetch_related('subcategory_set__product_set').all()
    web_setting = Banner.objects.all()
    for i in web_setting:
        web_name = i.web_name
    return locals()
