from django import forms 
from .models import *

class  ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))
    phonenumber = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    class Meta:
        model = Contact
        fields = ['name','email','phonenumber','description']
        
        