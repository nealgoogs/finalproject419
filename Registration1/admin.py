from django.contrib import admin
from .models import UserCredentials1

@admin.register(UserCredentials1)
class UserCredentials1Admin(admin.ModelAdmin):
    list_display = ('username', 'password')  # Add other fields as necessary
