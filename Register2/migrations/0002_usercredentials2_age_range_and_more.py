# Generated by Django 4.2.7 on 2023-12-01 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercredentials2',
            name='age_range',
            field=models.CharField(blank=True, choices=[('under_18', 'Under 18'), ('18_30', '18-30'), ('31_40', '31-40'), ('41_50', '41-50'), ('51_60', '51-60'), ('above_60', '61 and above')], max_length=10),
        ),
        migrations.AddField(
            model_name='usercredentials2',
            name='cybersecurity_expertise',
            field=models.CharField(blank=True, choices=[('novice', 'Novice'), ('competent', 'Competent'), ('proficient', 'Proficient'), ('expert', 'Expert')], max_length=15),
        ),
        migrations.AddField(
            model_name='usercredentials2',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=20),
        ),
        migrations.AddField(
            model_name='usercredentials2',
            name='password_feedback',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usercredentials2',
            name='used_password_manager',
            field=models.BooleanField(default=False),
        ),
    ]
