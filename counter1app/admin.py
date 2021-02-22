from django.contrib import Amdin
# from .models import Contact

# Register your models here.

# admin.site.register(Group)
# admin.site.register(Contact)
from .models import Profile, Talking, Count, Add_user

# Register your models here.

admin.site.register(Talking)

admin.site.register(Profile)

admin.site.register(Count)

admin.site.register(Add_user)

