from django.contrib import admin
from .models import Profile, Talking, Count, Add_user

# Register your models here.

admin.site.register(Talking)

admin.site.register(Profile)

admin.site.register(Count)

admin.site.register(Add_user)
