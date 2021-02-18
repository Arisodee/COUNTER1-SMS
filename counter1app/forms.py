from django import forms
from .models import Group sending_sms

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name','contact']

#sending sms form user form

class sendingForm(forms.ModelForm):
    
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