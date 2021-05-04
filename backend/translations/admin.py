from django.contrib import admin
from .models import Project, Language, Translation

# Language
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "language_code")


admin.site.register(Language, LanguageAdmin)


# Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "repository_url")


admin.site.register(Project, ProjectAdmin)


# Translation
class TranslationAdmin(admin.ModelAdmin):
    list_display = ("text", "file_path", "object_path", "language")


admin.site.register(Translation, TranslationAdmin)
