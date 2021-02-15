from django import forms

from .models import Talking


class TalkingForm(forms.ModelForm):
    # api_key = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "api_key"}))
    
    class Meta:
        model = Talking
        fields = ['username', 'api_key', 'recepients', 'message', 
                  'sender_id'
                ]
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'api_key': forms.TextInput(attrs={'class': 'form-control'}),
            'recepients': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'}),
            'sebder_id': forms.TextInput(attrs={'class': 'form-control'}),
        }
    