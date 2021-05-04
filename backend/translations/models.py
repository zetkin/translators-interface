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


class Language(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    language_code = models.CharField(max_length=8, null=False, blank=False)


class Translation(models.Model):
    text = models.TextField(null=False, blank=False, unique=False)
    author = models.CharField(max_length=64, blank=False, null=False)
    from_repository = models.BooleanField(null=False, blank=False)
    # Relationship to repo
    file_path = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=False,
    )
    object_path = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=False,
    )
    # Links to project and language
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=False, blank=False
    )
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, null=False, blank=False
    )
