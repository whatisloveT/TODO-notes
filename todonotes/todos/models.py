from django.db import models
from Users.models import CustomUser


class Project(models.Model):
    title = models.CharField(max_length=64)
    link_to_git = models.URLField(blank=True)
    users = models.ManyToManyField(CustomUser)
    description = models.TextField(blank=True, null=True)


class Todo(models.Model):
    project = models.OneToOneField(Project,on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    user_created = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited", editable=False)
    is_active = models.BooleanField(default=True, verbose_name='active')
