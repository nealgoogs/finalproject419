# Generated by Django 4.2.7 on 2023-12-01 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration1', '0002_usercredentials1_password_strength'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercredentials1',
            name='age_range',
            field=models.CharField(blank=True, choices=[('under_18', 'Under 18'), ('18_30', '18-30'), ('31_40', '31-40'), ('41_50', '41-50'), ('51_60', '51-60'), ('above_60', '61 and above')], max_length=10),
        ),
        migrations.AddField(
            model_name='usercredentials1',
            name='cybersecurity_expertise',
            field=models.CharField(blank=True, choices=[('novice', 'Novice'), ('competent', 'Competent'), ('proficient', 'Proficient'), ('expert', 'Expert')], max_length=15),
        ),
        migrations.AddField(
            model_name='usercredentials1',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other'), ('prefer_not_to_say', 'Prefer not to say')], max_length=20),
        ),
        migrations.AddField(
            model_name='usercredentials1',
            name='password_feedback',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usercredentials1',
            name='used_password_manager',
            field=models.BooleanField(default=False),
        ),
    ]
