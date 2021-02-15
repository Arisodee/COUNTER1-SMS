from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.TextField(unique=True)
    last_name = models.TextField()
    email = models.TextField()
    mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)