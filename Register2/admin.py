from django.contrib import admin
from .models import UserCredentials2

@admin.register(UserCredentials2)
class UserCredentials2Admin(admin.ModelAdmin):
    list_display = ('username', 'password_strength', 'gender', 'age_range', 'cybersecurity_expertise', 'used_password_manager', 'password_feedback')
