from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from translations.models import Translation, Language, Project

from .factories import LanguageFactory, ProjectFactory


class TestProjectViews(APITestCase):
    def setUp(self):

        english = LanguageFactory(name="English", language_code="en")
        swedish = LanguageFactory(name="Swedish", language_code="sv")

        self.project1 = ProjectFactory(languages=(english, swedish))
        self.project2 = ProjectFactory(languages=(english, swedish))

        self.client = APIClient()

    def test_success_list_projects(self):
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_success_retrieve_project(self):
        response = self.client.get("/projects/{}/".format(self.project1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.project1.name)
