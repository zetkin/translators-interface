import os

from translations.models import Project, Translation
from .filter_latest_translations import filter_latest_translations


def generate_locale_files(project: Project, path: str):
    # Move working dir to the one provided
    os.chdir(path)

    # Get all latest translations for project
    project_translations = Translation.objects.filter(project=project)
    latest_project_translations = filter_latest_translations(project_translations)

    # Create file structure
    for translation in latest_project_translations:
        # If file not in root directory
        if len(translation.file_path.split("/")[:-1]) > 1:
            # Make folders
            try:
                os.mkdir("/".join(translation.file_path.split("/")[1:-1]))
            except FileExistsError:
                pass
        # Create file
        try:
            os.mknod(translation.file_path)
        except FileExistsError:
            pass

    # Group translations that are in the same file and make file structure
    translations_grouped = {}
    for translation in latest_project_translations:

        if not translations_grouped.get(translation.file_path):
            translations_grouped[translation.file_path] = {}

    # Open each file and write translations
