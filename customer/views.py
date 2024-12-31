from django.shortcuts import render, HttpResponse
from math import ceil
from administrator.models import *

def dashboard(request):
    categories = Category.objects.prefetch_related('subcategory_set__product_set').all()
    unique_categories = {}
    for category in categories:
        if category.category_name not in unique_categories:
            unique_categories[category.category_name] = category
    category_list = list(unique_categories.values())
    all_data = []
    
    processed_categories = set()
    for i in range(0, len(category_list), 4):
        box_categories = [
            category for category in category_list[i:i + 4]
            if category not in processed_categories
        ]
        boxes = []
        for category in box_categories:
            subcategories = category.subcategory_set.all()[:4]
            unique_products = []
            for subcategory in subcategories:
                product = subcategory.product_set.first()
                if product:
                    unique_products.append(product)
            boxes.append({
                'category': category,
                'products': unique_products,
            })
            processed_categories.add(category)
        if boxes:
            all_data.append({'type': 'boxes', 'boxes': boxes})
        if i + 4 < len(category_list):
            slide_category = category_list[i + 4]
            if slide_category not in processed_categories:
                subcategories = slide_category.subcategory_set.all()
                unique_slide_products = []
                for subcategory in subcategories:
                    product = subcategory.product_set.first()
                    if product:
                        unique_slide_products.append(product)
                product_batches = [
                    unique_slide_products[j:j + 5] for j in range(0, len(unique_slide_products), 5)
                ]
                all_data.append({
                    'type': 'slide',
                    'category': slide_category,
                    'product_batches': product_batches,
                    'slide_range': range(1, len(product_batches))
                })
                processed_categories.add(slide_category)
    return render(request, 'dashboard.html', locals())

def categoryProducts(request, category_name):
    category_products = Product.objects.filter(sub_category__sub_category_name = category_name)
    for product in category_products:
        discount_percentage = float(product.discount_percentage) if product.discount_percentage else 0
        discount_amount = float(product.price) * (discount_percentage / 100)
        product.discounted_price = float(product.price) - discount_amount 
    return render(request, 'category_products.html', locals())