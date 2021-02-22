from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
from django import forms
from .models import Add_user


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=60)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

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


