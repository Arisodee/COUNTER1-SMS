from django.contrib import admin
from .models import Profile, Talking, Count

# Register your models here.

admin.site.register(Talking)

admin.site.register(Profile)

admin.site.register(Count)
