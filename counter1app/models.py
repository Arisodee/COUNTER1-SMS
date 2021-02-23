
# Create your models here.
from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=150,unique=True)
    
    def __str__(self):
        return self.first_name

class Group(models.Model):
    name = models.CharField(max_length = 50)
    contact = models.ForeignKey(Profile,on_delete =models.CASCADE, null = True)

    def __str__(self):
        return self.name
    

    def save_group(self):
        self.save()
    
    def delete_group(self):
        self.delete()
    
    @classmethod
    def get_groups(cls):
       groups = Group.objects.all()
       return groups
    
    @classmethod
    def search_by_name(cls,search_term):
        results = cls.objects.filter(name__icontains = search_term)
        return results

