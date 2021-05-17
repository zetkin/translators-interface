from github import Github
from decouple import config

from translations.models import Project, Language, Translation


def create_pull_request(project):
    GITHUB_ACCESS_TOKEN = config("GITHUB_ACCESS_TOKEN")
    # Access git repo for project
    g = Github(GITHUB_ACCESS_TOKEN)
    repo = g.get_repo(project.repository_name)

    # Make a folder for the repo to clone in
    # If folder already exists there, throw an error

    # Delete all localisation files

    # Make

    # Create PR
    # pr = repo.create_pull(
    #     title="Use 'requests' instead of 'httplib'",
    #     body=body,
    #     head="develop",
    #     base="master",
    # )
