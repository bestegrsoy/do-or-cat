# Generated by Django 5.1.5 on 2025-01-15 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_service', '0006_users_access_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='refresh_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]