# Generated by Django 5.1.4 on 2025-01-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_service', '0002_alter_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
