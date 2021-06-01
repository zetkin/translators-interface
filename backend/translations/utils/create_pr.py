import os
import tempfile
import shutil
from datetime import datetime

import git
from github import Github
from decouple import config

from translations.models import Project
from translations.utils.generate_locale_files import generate_locale_files


def create_pr(project: Project):
    GITHUB_ACCESS_TOKEN = config("GITHUB_ACCESS_TOKEN")

    g = Github(GITHUB_ACCESS_TOKEN)
    repo = g.get_repo(project.repository_name)

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create git url with username and password
        username = "djbusstop"
        # git://github.com/zetkin/app.zetkin.org.git
        remote = "https://{}:{}@{}".format(
            username, GITHUB_ACCESS_TOKEN, "".join(repo.git_url.split("git://"))
        )

        local_repo = git.Repo.clone_from(remote, tmpdir, branch="main")
        # Check out new branch for changes
        branch_name = "translations_{}".format(datetime.now().isoformat(sep="_"))
        local_repo.git.checkout("HEAD", b=branch_name)

        # Delete contents at the existing locale folder
        path_to_locales = os.path.join(tmpdir, project.locale_files_path)
        shutil.rmtree(path_to_locales)
        # Create new folder for locales
        os.mkdir(path_to_locales)

        generate_locale_files(project, path_to_locales)

        local_repo.git.add(path_to_locales)

        # Need to set credentials
        local_repo.git.config("--global", "user.email", "you@example.com")
        local_repo.git.config("--global", "user.name", "fakename")

        local_repo.git.commit("-m", "translations")
        local_repo.git.push("--set-upstream", "origin", branch_name)
