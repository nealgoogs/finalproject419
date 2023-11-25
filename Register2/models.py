from django.db import models

class UserCredentials2(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password_strength = models.IntegerField(default=0)  # Add this field
