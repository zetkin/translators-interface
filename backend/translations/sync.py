from .models import Project, Language, Translation

"""
Syncing with the git repo.

"""


def sync(project: Project):
    # Access git repo for project
    print(project)
