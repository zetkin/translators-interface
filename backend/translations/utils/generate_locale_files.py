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
        # Split file path
        file_path_parts = translation.file_path.split("/")[:-1]

        # If file not in root of directory
        if len(file_path_parts) > 1:
            for file_path_part in file_path_parts:
                print
                # Make folders for each part, if not already existing
                # try:
                os.mkdir(file_path_part)
                # os.chdir(file_path_part)
                # except:
