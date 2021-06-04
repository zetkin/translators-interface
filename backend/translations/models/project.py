from django.db import models
from rest_framework import serializers
from django.utils.timezone import now

from .language import Language, LanguageSerializer


class Project(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    repository_name = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        unique=False,
        help_text="The repo name including the project if there is one. For example 'zetkin/organize.zetk.in'",
    )
    locale_files_path = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=False,
        help_text="Path to the locale files within the project. Use this format 'src/locale'.",
    )
    languages = models.ManyToManyField(Language)
    last_sync_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = (
            "repository_name",
            "locale_files_path",
        )

    def __str__(self):
        return self.name


class ProjectSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = "__all__"
