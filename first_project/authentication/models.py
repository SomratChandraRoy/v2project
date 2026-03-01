from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Author(AbstractUser):
    bio = models.TextField(max_length=2000, blank=True, default="")
    subtitle = models.CharField(max_length=200, blank=True, default="")
    image = models.ImageField(upload_to="author/pfp/", blank=True, null=True)
