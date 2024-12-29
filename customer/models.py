from django.db import models

class CustomerProfile(models.Model):
    customer_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50, blank = True, null = True)
    profile_picture = models.ImageField(upload_to = 'profile_pictures/', blank = True, null = True)
    email = models.EmailField(unique = True)
    date_of_birth = models.DateField(blank = True, null = True)
    contact_number = models.CharField(max_length = 15, unique = True)
    address = models.TextField(blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return f"{self.first_name} {self.last_name or ''}".strip()