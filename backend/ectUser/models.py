from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class EctUser(AbstractUser):
    ROLE_CHOICE = [('Admin', 'Admin User'),
                   ('StdUser', 'Standard User'), ('Guest', 'Guest')]

    role = models.CharField(
        max_length=20, choices=ROLE_CHOICE, default='Guest')
