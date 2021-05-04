from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    repository_url = models.URLField(
        null=False,
        blank=False,
        unique=False,
    )
    locale_files_path = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=False,
    )
