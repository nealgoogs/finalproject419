# Generated by Django 4.2.7 on 2023-11-25 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercredentials1',
            name='password_strength',
            field=models.IntegerField(default=0),
        ),
    ]