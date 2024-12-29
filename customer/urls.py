from django.urls import path
from customer import views

urlpatterns = [
    path('home/', views.customerHome, name = 'home'),
]