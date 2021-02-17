from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.TextField(unique=True)
    last_name = models.TextField()
    email = models.TextField()
    mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='new_post/', blank = 'true')
    bio = models.TextField()
 
    def save_profile(self):
        self.save
    def delete_user(self):
        self.delete()
    def __str__(self):
        return f'{self.user.username} Profile'





class Add_user(models.Model):
    full_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=8, unique=True)
    phone_number = models.CharField(max_length=10, unique=True,default=None)
    email = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.full_name


