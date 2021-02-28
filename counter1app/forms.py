from django import forms
from .models import Talking, Add_user, Group, Profile, Sending, Schedule

from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  

class TalkingForm(forms.ModelForm):

    class Meta:
        model = Talking
        fields = ['recipients', 'message', 'topup_amount', 
                  
                ]

        widgets = {
          
            'recipients': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'}),
            'topup_amount': forms.TextInput(attrs={'class': 'form-control'}),
        
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


        widgets = {
          
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        
        }


class EditSupervisor(forms.ModelForm):
    class Meta:
        model = Add_user
        fields = ('full_name', 'id_number','phone_number', 'email')

        widgets = {
          
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name','last_name','email','phone')


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name','contact']


class SendingForm(forms.ModelForm):
    class Meta:
        model = Sending
        fields = ['recipients', 'message',
                ]
        widgets = {
            'recipients': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'}),
        }
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
    
