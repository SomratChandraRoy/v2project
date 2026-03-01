from django.db import models


# Create your models here.
class Video(models.Model):
    video = models.FileField(upload_to="video_conversion/input")
    title = models.CharField(max_length=200)


class Audio(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)
    audio = models.FileField(upload_to="video_conversion/output")
    title = models.CharField(max_length=200)
