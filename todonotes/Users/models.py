from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(verbose_name='email address',max_length=255,unique= True, blank=True)
