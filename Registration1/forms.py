from django import forms
from .models import UserCredentials1

class UserRegistrationForm1(forms.ModelForm):
    class Meta:
        model = UserCredentials1
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
