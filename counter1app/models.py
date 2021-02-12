from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=150,unique=True)
    
    def __str__(self):
        return self.first_name