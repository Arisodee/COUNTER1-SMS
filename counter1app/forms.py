from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  


class SignUpForm(UserCreationForm):  
    class Meta:  
        model = User  
        fields = ('email', 'first_name', 'last_name', 'username')