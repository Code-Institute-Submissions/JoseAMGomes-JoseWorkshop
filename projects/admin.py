from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'rating',
        'images',
    )

    ordering = ('sku',)


# Register your models here.
admin.site.register(Project, ProjectAdmin)