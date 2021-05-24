import os
import glob
import tempfile
from datetime import datetime

import git
from github import Github
from decouple import config

from translations.models import Project, Language, Translation


def create_pr(project: Project):
    GITHUB_ACCESS_TOKEN = config("GITHUB_ACCESS_TOKEN")

    g = Github(GITHUB_ACCESS_TOKEN)
    repo = g.get_repo(project.repository_name)

    # Clone repo to temp folder
    repo_dir = tempfile.TemporaryDirectory()
    local_repo = git.Repo.clone_from(repo.git_url, repo_dir, branch="master")

    # Check out new branch for changes
    branch_name = "translations_{}".format(datetime.now().isoformat())
    local_repo.head.reference = local_repo.create_head(branch_name)

    # try:
    # Move to the local directory for the project
    working_dir = os.path.join(repo_dir.name, project.locale_files_path)
    os.chdir(working_dir)
    print(os.getcwd())
    # except:

    #     pass

    # Remove temp dir at end of process
    repo_dir.cleanup()
