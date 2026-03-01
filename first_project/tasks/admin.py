from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Task


@admin.register(Task)
class TaskAdmin(ModelAdmin):
    list_display = ("task", "author", "is_complete")
    list_filter = ("is_complete", "author")
    search_fields = ("task", "author__username")
    list_editable = ("is_complete",)
    ordering = ("is_complete", "-pk")
    list_per_page = 25
    list_filter_submit = True
