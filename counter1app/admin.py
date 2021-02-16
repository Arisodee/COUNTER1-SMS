from django.contrib import admin
from .models import Profile

from .models import Talking

# Register your models here.

admin.site.register(Talking)

admin.site.register(Profile)
