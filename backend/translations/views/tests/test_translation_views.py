import logging
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from translations.models import Translation, Language, Project

from translations.models.factories import (
    LanguageFactory,
    ProjectFactory,
    TranslationFactory,
)


class TestTranslationViews(APITestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

        self.english = LanguageFactory(name="English", language_code="en")
        self.swedish = LanguageFactory(name="Swedish", language_code="sv")

        self.project1 = ProjectFactory(languages=(self.english, self.swedish))
        self.project2 = ProjectFactory(languages=(self.english, self.swedish))

        TranslationFactory.create_batch(size=100, project=self.project1)
        TranslationFactory.create_batch(size=100, project=self.project2)

        self.client = APIClient()

    def test_success_list_all_translations(self):
        response = self.client.get("/translations/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 200)

    def test_success_list_project_translations_for_language(self):
        url = "/translations/?language={}&project={}".format(
            self.english.id, self.project1.id
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Half of project 1's translations are in English
        self.assertEqual(len(response.data), 50)

    def test_fail_put_patch_delete(self):
        translation = TranslationFactory()

        put_response = self.client.put(
            "/translations/{}/".format(translation.id), {"author": "new author"}
        )
        self.assertEqual(put_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        patch_response = self.client.patch(
            "/translations/{}/".format(translation.id), {"author": "new author"}
        )
        self.assertEqual(patch_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        delete_response = self.client.delete(
            "/translations/{}/".format(translation.id), {"author": "new author"}
        )
        self.assertEqual(
            delete_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_success_create_translation(self):
        post_response = self.client.post(
            "/translations/",
            {
                "text": "example text",
                "author": "new author",
                "from_repository": False,
                "file_path": "./en.yaml",
                "object_path": "path.to.key",
                "project": self.project1.id,
                "language": self.english.id,
            },
            format="json",
        )

        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
