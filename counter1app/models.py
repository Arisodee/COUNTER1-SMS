from __future__ import print_function

from django.db import models

import africastalking


class Talking(models.Model):
    username = models.CharField(max_length=200, blank=True, null=True)
    api_key = models.CharField(max_length=201, blank=True, null=True)
    recepients = models.TextField(max_length=1000, blank=True, null=True)
    message = models.TextField(max_length=200, blank=True, null=True)
    sender_id = models.CharField(max_length=200, blank=True, null=True)
    
    
    def __str__(self):
        return username
    
    
    def save(self, *args, **kwargs):     
        
        username      = self.username
        api_key    = self.api_key

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        self.recepients
        self.message
        self.sender_id

        try:
            # Thats it, hit send and we'll take care of the rest.
            response = self.message.send(message, recepients, sender_id)
            print (response)
        except Exception as e:
            print ('Encountered an error while sending: %s' % str(e))

            return super(Talking, self).save(*args, **kwargs)


    
    

          
      

          
       