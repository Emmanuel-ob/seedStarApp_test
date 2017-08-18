from django import forms
from .models import UserAccount

class AddForm(forms.ModelForm):
    
    name = forms.CharField(max_length = 120, help_text = '',  widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Your Name', 'required': 'required'}))
    email = forms.EmailField(max_length = 120,  help_text = '',  widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'email@example.com', 'required': 'required'}))
   
    class Meta:
        model = UserAccount
        fields = ('name', 'email',)

