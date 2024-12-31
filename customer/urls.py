from django.urls import path
from customer import views

urlpatterns = [
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('<str:category_name>/products', views.categoryProducts, name = 'cat_products'),
]