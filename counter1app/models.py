from django.db import models

# Create your models here.
class Count(models.Model):
    username = models.CharField(max_length=80)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.username)