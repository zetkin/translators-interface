import yaml
from django.db.utils import IntegrityError
from decouple import config
from github import Github, ContentFile
from pandas import json_normalize

from .models import Project, Language, Translation

"""
Syncing the Translation objects with the git repo for a project.
This function creates Translation records for every key in a project's
localisation files for languages that are configured.
"""


def sync(project: Project):
    GITHUB_ACCESS_TOKEN = config("GITHUB_ACCESS_TOKEN")
    # Access git repo for project
    g = Github(GITHUB_ACCESS_TOKEN)
    repo = g.get_repo(project.repository_name)
    contents = repo.get_contents(project.locale_files_path)

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
        # Get language
        language_code = relative_filepath.split("/")[-1].split(".")[0]
        # Get commit date for file
        commit = repo.get_commits(path=file.path)[0].commit
        commit_date = commit.committer.date
        # If language in the project languages
        if language_code in [lang.language_code for lang in project.languages.all()]:
            file_object = yaml.safe_load(file.decoded_content)
            flat_file_object = json_normalize(file_object, sep=".").to_dict(
                orient="records"
            )[0]
            # Loop through each translation key/value pair and create translation object
            for key, value in flat_file_object.items():
                if isinstance(value, str):
                    language = Language.objects.get(language_code=language_code)
                    try:
                        translation = Translation.objects.create(
                            text=value,
                            author="",
                            from_repository=True,
                            file_path=relative_filepath,
                            object_path=key,
                            project=project,
                            language=language,
                            created_at=commit_date,
                        )
                    # If translation with file_path, object_path & created_at exists
                    except IntegrityError:
                        pass
