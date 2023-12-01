from django import forms
from .models import UserCredentials2

class UserRegistrationForm2(forms.ModelForm):
    class Meta:
        model = UserCredentials2
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class SurveyForm(forms.ModelForm):
    class Meta:
        model = UserCredentials2
        fields = ['gender', 'age_range', 'cybersecurity_expertise', 'used_password_manager', 'password_feedback']
        widgets = {
            'gender': forms.Select,
            'age_range': forms.Select,
            'cybersecurity_expertise': forms.Select,
            'used_password_manager': forms.Select(
                choices=[
                    (True, 'Yes'),
                    (False, 'No')
                ]
            ),
            'password_feedback': forms.Textarea(
                attrs={'placeholder': 'Write your opinions about the password manager here'}
            ),
        }