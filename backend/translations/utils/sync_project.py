import yaml
from typing import Dict
from django.db.utils import IntegrityError
from django.utils.timezone import now
from decouple import config
from github import Github
from pandas import json_normalize
from yaml.loader import BaseLoader
from yaml import scanner

from translations.models import Project, Language, Translation
from .filter_latest_translations import filter_latest_translations
from .mark_deleted_translations import mark_deleted_translations


def sync_project(project: Project):
    """
    Syncing the Translation objects with the git repo for a project.
    This function creates Translation records for every key in a project's
    localisation files for languages that are configured.
    """

    sync_time = now()

    GITHUB_ACCESS_TOKEN = config("GITHUB_ACCESS_TOKEN")
    # Access git repo for project
    g = Github(GITHUB_ACCESS_TOKEN)
    repo = g.get_repo(project.repository_name)
    contents = repo.get_contents(project.locale_files_path)

    # Get previous translations
    previous_translations = filter_latest_translations(
        Translation.objects.filter(project=project)
    )

    # Collect all translations in project, to check which translations are removed
    all_translations_in_project: Dict[str, Dict[str, Translation]] = {}

    # Get all files recursively from the repo
    files = []
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            files.append(file_content)

    for file in files:
        # The file path relative to the locale files directory for the project
        relative_filepath = file.path.replace(project.locale_files_path, ".")
        # Add file path to all translations dict
        all_translations_in_project[relative_filepath] = {}
        # Get language
        language_code = relative_filepath.split("/")[-1].split(".")[0]
        # Get commit date for file
        commit = repo.get_commits(path=file.path)[0].commit
        commit_date = commit.committer.date
        # If language in the project languages
        if language_code in [lang.language_code for lang in project.languages.all()]:
            try:
                file_object = yaml.load(file.decoded_content, Loader=BaseLoader)
                flat_file_object = json_normalize(
                    file_object, sep=".", errors="ignore"
                ).to_dict(orient="records")[0]
                # Loop through each translation key/value pair and create translation object
                for key, value in flat_file_object.items():
                    if isinstance(value, str):
                        language = Language.objects.get(language_code=language_code)
                        try:
                            translation = Translation(
                                text=value,
                                author="",
                                from_repository=True,
                                file_path=relative_filepath,
                                object_path=key,
                                project=project,
                                language=language,
                                created_at=commit_date,
                            )

                            # Add translation to all translations in project
                            all_translations_in_project[relative_filepath][
                                key
                            ] = translation

                            # Attempt to create translation, will be ignored if translation already in project
                            translation.save()
                        # If translation with file_path, object_path & created_at exists, ignore save
                        except IntegrityError:
                            pass
            except scanner.ScannerError:
                pass

    mark_deleted_translations(
        previous_translations, all_translations_in_project, sync_time
    )

    # When done, set the time the sync occurred
    project.last_sync_time = sync_time
    project.save()
