from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=100)
    bio = models.TextField(max_length=1000, blank=True, null=True) # blank=True, null=True means "not required"
    location = models.CharField(max_length=100)
    skills = models.ManyToManyField(
        to="skills.Skill",
        related_name="users_with_skill"
    )