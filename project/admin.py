from django.contrib import admin
from .models import Project

# Register your models here.

admin.site.site_header = "Felipe Rebon"

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_upload', 'is_visible', 'view_order')
    search_fields = ('title', 'presentation_text', 'text')
    ordering = ('is_visible', 'view_order', 'date_upload')


    fieldsets = (
        ('Affichage', {
            'fields': (('view_order', 'is_visible'),)
        }),
        ('Infos du projet', {
            'fields': ('title', 'presentation_text', 'date_project', 'background',)
        }),
        ('Contenu du projet', {
            'fields': ('image', 'video', 'text')
        })
    )


admin.site.register(Project, ProjectAdmin)
