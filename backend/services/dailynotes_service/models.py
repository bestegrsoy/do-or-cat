from django.db import models

class dailynotes(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    owner_mail = models.ForeignKey('auth_service.Users', on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mission_date = models.DateField(null=True, blank=True)