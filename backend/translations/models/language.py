from django.db import models
from rest_framework import serializers


class Language(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    language_code = models.CharField(max_length=8, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"
