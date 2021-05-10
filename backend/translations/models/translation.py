from django.db import models
from django.utils.timezone import now
from rest_framework import serializers

from translations.utils.build_dotpath import build_dotpath

from .language import Language, LanguageSerializer
from .project import Project, ProjectSerializer


class Translation(models.Model):
    text = models.TextField(null=False, blank=False, unique=False)
    author = models.CharField(max_length=64, blank=False, null=False)
    from_repository = models.BooleanField(null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=False, default=now)
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
        return build_dotpath(self.file_path, self.object_path)

    class Meta:
        unique_together = (
            "file_path",
            "object_path",
            "created_at",
            "project",
        )


class TranslationSerializer(serializers.ModelSerializer):
    """
    Get request returns the entire language object, but post request takes the language id
    """

    dotpath = serializers.ReadOnlyField()

    class Meta:
        model = Translation
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["language"] = LanguageSerializer(instance.language).data
        return response
