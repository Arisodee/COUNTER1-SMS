from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 50)
    number = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length = 50)
    contact = models.ForeignKey(Contact,on_delete =models.CASCADE, null = True)

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
