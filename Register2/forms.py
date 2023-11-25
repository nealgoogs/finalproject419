from django import forms
from .models import UserCredentials2

class UserRegistrationForm2(forms.ModelForm):
    class Meta:
        model = UserCredentials2
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
