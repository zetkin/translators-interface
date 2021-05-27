import os

from translations.models import Project, Translation
from .filter_latest_translations import filter_latest_translations


def generate_locale_files(project: Project, path: str):
    # Move working dir to the one provided
    os.chdir(path)

    # Get all latest translations for project
    project_translations = Translation.objects.filter(project=project)
    latest_project_translations = filter_latest_translations(project_translations)

    for translation in latest_project_translations:
        # If file not in root directory
        if len(translation.file_path.split("/")[:-1]) > 1:
            # Make folders for file
            try:
                os.mkdir(translation.file_path.split("/")[1:-1].join("/"))
            except FileExistsError:
                pass
            os.mknod(translation.file_path)
