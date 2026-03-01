from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Video, Audio


@admin.register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ("title", "video")
    search_fields = ("title",)
    ordering = ("-pk",)


@admin.register(Audio)
class AudioAdmin(ModelAdmin):
    list_display = ("title", "video", "audio")
    search_fields = ("title",)
    list_filter = ("video",)
    ordering = ("-pk",)
