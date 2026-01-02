from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Resource, Subject, SubjectResourceJoin, Comment

# Register your models here.


class SubjectResourceInline(admin.TabularInline):
    """
    Provides ability to edit related objects in a table style layout

    ``model``
        Each inline row corresponds to one **SubjectResourceJoin** record
        *Must be a Model class*
    ``extra``
        Additional rows shown as default
    """

    model = SubjectResourceJoin
    extra = 1


@admin.action(description="Mark all as published")
def mark_all_published(modeladmin, request, queryset):
    queryset.update(status="p")


@admin.register(Resource)
class ResourceAdmin(SummernoteModelAdmin):
    """Customizes the admin interface for the Post model.
    It uses Summernote for the 'content' field and provides
    list display, search, filtering, and slug prepopulation.
    """

    inlines = [SubjectResourceInline]
    actions = [mark_all_published]

    list_display = ("title", "slug", "status", "created_on", "author")
    search_fields = ["title", "content"]
    list_filter = ("status", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


admin.site.register(Subject)
admin.site.register(Comment)
