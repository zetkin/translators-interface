import os
import yaml

from translations.models import Project, Translation
from .filter_latest_translations import filter_latest_translations


def put(d, keys, item):
    if "." in keys:
        key, rest = keys.split(".", 1)
        if key not in d:
            d[key] = {}
        put(d[key], rest, item)
    else:
        d[keys] = item


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

    # Group translations that are in the same file and make file contents
    translations_files = {}
    for translation in latest_project_translations:
        # Create item in translations
        if not translations_files.get(translation.file_path):
            translations_files[translation.file_path] = {}

        put(
            translations_files[translation.file_path],
            translation.object_path,
            translation.text,
        )

    # Write each items contents in YAML
    for file_path in translations_files:
        # Create YAML
        yaml_contents = yaml.dump(
            translations_files[file_path], default_flow_style=False
        )
        # Write files
        f = open(file_path, "a")
        f.write(yaml_contents)
        f.close()
