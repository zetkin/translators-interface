import os
import tempfile
import shutil
from django.contrib import admin, messages
from django.http import HttpResponse

from .models import Project, Language, Translation
from .utils.sync_project import sync_project
from .utils.create_pr import create_pr
from .utils.generate_locale_files import generate_locale_files

# Language
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "language_code")


admin.site.register(Language, LanguageAdmin)


# Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "repository_name", "last_sync_time")
    readonly_fields = ["last_sync_time"]

    actions = ["sync", "export_translations"]

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

    @admin.action(description="Export locale files")
    def export_translations(self, request, queryset):
        # Temp directory for generated translations
        with tempfile.TemporaryDirectory() as tmpdir:
            for project in queryset.all():
                # Create folder for each project's translations
                path = os.path.join(tmpdir, "{}".format(project.name))
                os.mkdir(path)
                # Generate translation files in project folder
                generate_locale_files(project, path)

            # Temp directory for zipped translations
            with tempfile.TemporaryDirectory() as tmp_zip_dir:
                os.chdir(tmp_zip_dir)
                zip = shutil.make_archive(
                    base_name="locales_export",
                    format="zip",
                    root_dir=tmpdir,
                )

                # Serve zipped translations
                with open(zip, "rb") as fh:
                    response = HttpResponse(
                        fh.read(), content_type="multipart/form-data"
                    )
                    response[
                        "Content-Disposition"
                    ] = "inline; filename=locales_export.zip"
                    return response


admin.site.register(Project, ProjectAdmin)


# Translation
class TranslationAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "dotpath",
        "language",
        "created_at",
    )
    list_filter = ["language", "project"]


admin.site.register(Translation, TranslationAdmin)
