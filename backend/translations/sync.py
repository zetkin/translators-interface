from decouple import config
from github import Github

from .models import Project, Language, Translation

"""
Syncing with the git repo.

"""


def sync(project: Project):
    GITHUB_ACCESS_TOKEN = config("GITHUB_ACCESS_TOKEN")
    # Access git repo for project
    g = Github(GITHUB_ACCESS_TOKEN)
    repo = g.get_repo(project.repository_name)
    print(repo)
