from django.contrib import admin
from .models import UserCredentials2

@admin.register(UserCredentials2)
class UserCredentials2Admin(admin.ModelAdmin):
    list_display = ('username', 'password')  # Add other fields as necessary
