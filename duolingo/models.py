from django.db import models
# models.py
class UserProfile(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    interested_language = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username

# Create your models here.
