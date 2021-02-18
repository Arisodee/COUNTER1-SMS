from django.db import models

# Create your models here.
class Add_user(models.Model):
    full_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=8, unique=True)
    phone_number = models.CharField(max_length=10, unique=True,default=None)
    email = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.full_name


