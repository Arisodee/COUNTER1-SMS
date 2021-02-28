from django import forms
from .models import Talking, Add_user,Schedule

from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  

class TalkingForm(forms.ModelForm):

    class Meta:
        model = Talking
        fields = ['recipients', 'message', 
                  
                ]

        widgets = {
            # 'username': forms.TextInput(attrs={'class': 'form-control'}),
            # 'api_key': forms.TextInput(attrs={'class': 'form-control'}),
            'recipients': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'}),
            # 'sender_id': forms.TextInput(attrs={'class': 'form-control'}),
        }
    

class SignUpForm(UserCreationForm):  
    class Meta:  
        model = User  
        fields = ('email', 'first_name', 'last_name', 'username')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']


class Add_userForm(forms.ModelForm):
    class Meta:
        model = Add_user
        fields = ('full_name', 'id_number','phone_number', 'email')


class EditSupervisor(forms.ModelForm):
    class Meta:
        model = Add_user
        fields = ('full_name', 'id_number','phone_number', 'email')

class SchedulingForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = [ 'date','recipients','message', 'time',
                  
                ]

        widgets = {
          
            'message': forms.TextInput(attrs={'class': 'form-control'}),
            'recipients': forms.TextInput(attrs={'class': 'form-control'}),
            'time' : forms.TextInput(attrs={'class': 'form-control'}),
            'date' : forms.DateInput(attrs={'class' : 'form-control'}),
            
        }
    
