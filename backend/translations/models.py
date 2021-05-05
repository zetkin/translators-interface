from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    language_code = models.CharField(max_length=8, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


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
    languages = models.ManyToManyField(Language)

    class Meta:
        unique_together = (
            "repository_url",
            "locale_files_path",
        )

    def __str__(self):
        return self.name


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

    # Joins the file path with the object path to create
    # the same dotpath format used in i18n software.
    @property
    def dotpath(self):
        file_dotpath_parts = self.file_path.split("/")[1:-1]
        if len(file_dotpath_parts) == 0:
            return self.object_path

        file_dotpath = ".".join(file_dotpath_parts)
        return "{}.{}".format(file_dotpath, self.object_path)

    class Meta:
        unique_together = (
            "file_path",
            "object_path",
        )
