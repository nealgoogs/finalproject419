# Generated by Django 4.2.7 on 2023-12-01 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registration1', '0003_usercredentials1_age_range_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercredentials1',
            name='age_range',
        ),
        migrations.RemoveField(
            model_name='usercredentials1',
            name='cybersecurity_expertise',
        ),
        migrations.RemoveField(
            model_name='usercredentials1',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='usercredentials1',
            name='password_feedback',
        ),
        migrations.RemoveField(
            model_name='usercredentials1',
            name='used_password_manager',
        ),
        migrations.CreateModel(
            name='SurveyResponse1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=20)),
                ('age_range', models.CharField(blank=True, choices=[('under_18', 'Under 18'), ('18_30', '18-30'), ('31_40', '31-40'), ('41_50', '41-50'), ('51_60', '51-60'), ('above_60', '61 and above')], max_length=10)),
                ('cybersecurity_expertise', models.CharField(blank=True, choices=[('novice', 'Novice'), ('competent', 'Competent'), ('proficient', 'Proficient'), ('expert', 'Expert')], max_length=15)),
                ('used_password_manager', models.BooleanField(default=False)),
                ('password_feedback', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration1.usercredentials1')),
            ],
        ),
    ]
