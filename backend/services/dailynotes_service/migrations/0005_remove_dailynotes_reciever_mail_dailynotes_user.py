# Generated by Django 5.1.5 on 2025-01-17 10:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailynotes_service', '0004_dailynotes_reciever_mail'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailynotes',
            name='reciever_mail',
        ),
        migrations.AddField(
            model_name='dailynotes',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='daily_notes', to=settings.AUTH_USER_MODEL),
        ),
    ]
