from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from translations.models import Translation, Language, Project


class TestTranslationViews(APITestCase):
    def setUp(self):
        english = Language.objects.create(name="English", language_code="en")
        swedish = Language.objects.create(name="Swedish", language_code="sv")
        self.project = Project.objects.create(
            name="Test Git Project",
            repository_name="zetkin/translators-interface",
            locale_files_path="backend/translations/tests/mock_locale_files",
        )
        self.project.languages.add(english)
        self.project.languages.add(swedish)
        self.project.save()

        self.client = APIClient()

    def test_success_list_projects(self):
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_success_retrieve_project(self):
        response = self.client.get("/projects/{}/".format(self.project1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Git Project")
