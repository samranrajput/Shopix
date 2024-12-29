from django.db import models

# Categories
class Category(models.Model):
    category_id = models.AutoField(primary_key = True)
    category_name = models.CharField(max_length = 100, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.category_name
    
# Sub Categories
class SubCategory(models.Model):
    sub_category_id = models.AutoField(primary_key = True)
    sub_category_name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.category.category_name} - {self.sub_category_name}"

# Products
class Product(models.Model):
    product_id = models.AutoField(primary_key = True)
    sub_category = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    product_name = models.CharField(max_length = 100)
    product_image = models.ImageField(upload_to = 'product_images/', blank = True, null = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    discount_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    discount_percentage = models.DecimalField(max_digits = 10, decimal_places = 2, null = True, blank = True)
    stock = models.PositiveIntegerField(default = 0)
    quantity = models.PositiveIntegerField(default = 1)
    description = models.TextField()
    is_available = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.product_name}"