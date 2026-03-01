from django.db import models
from authentication.models import Author


# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=300)
    is_complete = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
