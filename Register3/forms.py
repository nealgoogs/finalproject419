from django import forms
from .models import UserCredentials3

class UserRegistrationForm3(forms.ModelForm):
    class Meta:
        model = UserCredentials3
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
