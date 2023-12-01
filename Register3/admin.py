from django.contrib import admin
from .models import UserCredentials3

@admin.register(UserCredentials3)
class UserCredentials1Admin(admin.ModelAdmin):
    list_display = ('username', 'password_strength', 'gender', 'age_range', 'cybersecurity_expertise', 'used_password_manager', 'password_feedback')
