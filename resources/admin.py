from django.contrib import admin
from .models import Resource, Subject, SubjectResourceJoin

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


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    inlines = [SubjectResourceInline]


admin.site.register(Subject)
