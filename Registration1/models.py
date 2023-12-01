from django.db import models

class UserCredentials1(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password_strength = models.IntegerField(default=0)  # Add this field

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    AGE_RANGE_CHOICES = [
        ('under_18', 'Under 18'),
        ('18_30', '18-30'),
        ('31_40', '31-40'),
        ('41_50', '41-50'),
        ('51_60', '51-60'),
        ('above_60', '61 and above')
    ]

    EXPERTISE_LEVEL_CHOICES = [
        ('novice', 'Novice'),
        ('competent', 'Competent'),
        ('proficient', 'Proficient'),
        ('expert', 'Expert')
    ]

    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
    age_range = models.CharField(max_length=10, choices=AGE_RANGE_CHOICES, blank=True)
    cybersecurity_expertise = models.CharField(max_length=15, choices=EXPERTISE_LEVEL_CHOICES, blank=True)
    used_password_manager = models.BooleanField(default=False)
    password_feedback = models.TextField(blank=True, null=True)