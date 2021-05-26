from django.contrib import admin, messages

from .models import Project, Language, Translation
from .utils.sync_project import sync_project
from .utils.create_pr import create_pr

# Language
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "language_code")


admin.site.register(Language, LanguageAdmin)


# Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "repository_name")

    actions = ["sync", "create_pr"]

    @admin.action(description="Sync translations")
    def sync(self, request, queryset):
        for project in queryset.all():
            sync_project(project)
        self.message_user(request, "Sync successful", messages.SUCCESS)

    @admin.action(description="Create Pull Request")
    def create_pr(self, request, queryset):
        for project in queryset.all():
            create_pr(project)
        self.message_user(request, "Sync successful", messages.SUCCESS)


admin.site.register(Project, ProjectAdmin)


# Translation
class TranslationAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "dotpath",
        "language",
        "created_at",
    )


admin.site.register(Translation, TranslationAdmin)
