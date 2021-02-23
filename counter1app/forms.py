from django import forms
from .models import Group,Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name','last_name','email','phone')


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name','contact']
