from django.contrib import admin
from .models import Project, Language

# Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "repository_url")


admin.site.register(Project, ProjectAdmin)

# Language
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "language_code")


admin.site.register(Language, LanguageAdmin)
