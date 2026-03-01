from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import News, Page


@admin.register(News)
class NewsAdmin(ModelAdmin):
    list_display = ("title", "author", "created_time", "updated_time")
    list_filter = ("created_time", "author")
    search_fields = ("title", "content", "author__username")
    readonly_fields = ("created_time", "updated_time")
    ordering = ("-created_time",)
    list_per_page = 20
    list_filter_submit = True

    fieldsets = (
        ("Article", {"fields": ("title", "banner", "content")}),
        ("Author", {"fields": ("author",)}),
        ("Timestamps", {"fields": ("created_time", "updated_time")}),
    )


@admin.register(Page)
class PageAdmin(ModelAdmin):
    list_display = ("url", "views")
    search_fields = ("url",)
    ordering = ("-views",)
    readonly_fields = ("url", "views")
    list_per_page = 50
