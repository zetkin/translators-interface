import yaml
from decouple import config
from github import Github, ContentFile

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

    # Loop through files
    for file in files:
        print(file.decoded_content)

    # If file matches one of the projects supported languages, parse it
