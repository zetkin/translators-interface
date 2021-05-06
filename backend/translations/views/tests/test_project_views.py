from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from translations.models import Translation, Language, Project
from translations.sync import sync


class TestProjectViews(APITestCase()):
    def setUp(self):
        english = Language.objects.create(name="English", language_code="en")
        swedish = Language.objects.create(name="Swedish", language_code="sv")
        self.project1 = Project.objects.create(
            name="Test Git Project",
            repository_name="zetkin/translators-interface",
            locale_files_path="backend/translations/tests/mock_locale_files",
        )
        self.project1.languages.add(english)
        self.project1.languages.add(swedish)
        self.project1.save()

        self.project2 = Project.objects.create(
            name="Test Git Project",
            repository_name="zetkin/translators-interface",
            locale_files_path="backend/translations/tests/mock_locale_files",
        )
        self.project2.languages.add(english)
        self.project2.languages.add(swedish)
        self.project2.save()

    def test_success_list_projects(self):
        pass
