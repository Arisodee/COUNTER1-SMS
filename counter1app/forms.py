from django import forms
from .models import Talking

from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  

class TalkingForm(forms.ModelForm):
    
    class Meta:
        model = Talking
        fields = ['username', 'api_key', 'recipients', 'message', 
                  'sender_id'
                ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'api_key': forms.TextInput(attrs={'class': 'form-control'}),
            'recipients': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'}),
            'sender_id': forms.TextInput(attrs={'class': 'form-control'}),
        }
    

class SignUpForm(UserCreationForm):  
    class Meta:  
        model = User  
        fields = ('email', 'first_name', 'last_name', 'username')
