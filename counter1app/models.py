from __future__ import print_function

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

import json
import requests
from django.conf import settings


class Talking(models.Model):
    username = models.CharField(max_length=200, blank=True, null=True)
    api_key = models.CharField(max_length=201, blank=True, null=True)
    recipients = models.TextField(max_length=1000, blank=False, null=True)
    message = models.TextField(max_length=200, blank=False, null=True)
    sender_id = models.CharField(max_length=200, blank=True, null=True)
    topup_amount = models.CharField(max_length=200, blank=False, null=True) 


    
    def _str_(self):
        return self.username

    
    def save(self, *args, **kwargs):     

        url = 'https://api.sandbox.africastalking.com/version1/messaging'  
        
        headers = {
            'ApiKey': settings.API_KEY, 
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        
        data = {
            'username': 'sandbox',
            'from': '1234',
            'message': self.message,
            'to': self.recipients,
            'topup_amount': self.topup_amount,
        }

        def make_post_request():  
            response = requests.post(url=url, headers=headers, data=data )
            return response
        
        print( make_post_request().json() )

        return super(Talking, self).save(*args, **kwargs)

class Profile(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=150,unique=True)
    
    def __str__(self):
        return self.first_name


class Count(models.Model):
    username = models.CharField(max_length=80)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.username)




class Add_user(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=10,default=0)
    id_number = models.CharField(max_length=8, unique=True)
    phone_number = models.CharField(max_length=13, unique=True,default=None)
    email = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.full_name

class Group(models.Model):
    name = models.CharField(max_length = 50)
    contact = models.ManyToManyField(Profile)

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

