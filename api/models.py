from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    is_caregiver = models.BooleanField(default=False)
    is_senior = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name='user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Appointment(models.Model):
    caregiver = models.ForeignKey(User, related_name='caregiver_appointments', on_delete=models.CASCADE)
    senior = models.ForeignKey(User, related_name='senior_appointments', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
