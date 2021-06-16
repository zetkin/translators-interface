import os
import logging
import shutil
import tempfile
from distutils.dir_util import copy_tree

from django.test import TestCase

from translations.models import Translation, Language, Project
from translations.models.factories import (
    TranslationFactory,
    ProjectFactory,
    LanguageFactory,
)
from translations.utils.sync_project import sync_project


class SyncProjectTestCase(TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

        english = LanguageFactory(name="English", language_code="en")
        swedish = LanguageFactory(name="Swedish", language_code="sv")

        self.project = ProjectFactory(
            name="Test Git Project",
            repository_name="zetkin/translators-interface",
            locale_files_path="backend/translations/utils/tests/mock_files/sync_project",
            languages=(english, swedish),
        )

    def test_create_translations_from_git(self):
        sync_project(self.project)
        # Check 8 Swedish translations created
        swedish_translations = Translation.objects.filter(language__language_code="sv")
        self.assertEqual(len(swedish_translations), 8)
        # Check 8 English translations created
        english_translations = Translation.objects.filter(language__language_code="en")
        self.assertEqual(len(english_translations), 8)

        # Check a couple dotpath
        english_home_page_header_title = Translation.objects.get(
            language__language_code="en",
            file_path="./home_page/en.yaml",
            object_path="header.title",
        )
        self.assertEqual(
            english_home_page_header_title.dotpath, "home_page.header.title"
        )
        self.assertEqual(english_home_page_header_title.text, "Edit translations here")

        swedish_home_page_header_title = Translation.objects.get(
            language__language_code="sv",
            file_path="./home_page/sv.yaml",
            object_path="header.title",
        )
        self.assertEqual(
            swedish_home_page_header_title.dotpath, "home_page.header.title"
        )
        self.assertEqual(
            swedish_home_page_header_title.text, "Redigera översättningar här"
        )

    def test_handle_deleted_translations(self):
        """
        This is unfortunately a somewhat fragile test case because it depends on
        remote content that would be too complicated to mock.

        In order for this test to work, or if you need to change it, the mock
        translation files MUST be pushed to master. The sync only supports
        getting the repo data from master. IF THIS CHANGES, PLEASE UPDATE
         THIS DOCSTRING.

        Assumptions in test case:
            * All files have had new commits since the last sync.

        """
        # Sync project in current state
        sync_project(self.project)
        # Change locale files path to deleted, to mock deleted files
        self.project.locale_files_path = (
            "backend/translations/utils/tests/mock_files/handle_deleted_translations"
        )
        self.project.save()
        # Sync project again
        sync_project(self.project)

        # Check files that weren't deleted synced twice
        english_synced_translations = Translation.objects.filter(file_path="./en.yaml")
        swedish_synced_translations = Translation.objects.filter(file_path="./sv.yaml")

        self.assertEqual(english_synced_translations.count(), 10)
        self.assertEqual(swedish_synced_translations.count(), 10)

        # Assert all translations that would haven't been deleted have no "deleted_at"
        for translation in english_synced_translations:
            self.assertIsNone(translation.deleted_at)

        for translation in swedish_synced_translations:
            self.assertIsNone(translation.deleted_at)

        # Check files that were deleted only have synced once
        english_deleted_translations = Translation.objects.filter(
            file_path="./home_page/en.yaml"
        )
        swedish_deleted_translations = Translation.objects.filter(
            file_path="./home_page/sv.yaml"
        )

        self.assertEqual(english_deleted_translations.count(), 3)
        self.assertEqual(swedish_deleted_translations.count(), 3)

        # Assert all translations that would have been deleted are marked
        for translation in english_deleted_translations:
            self.assertIsNotNone(translation.deleted_at)

        for translation in swedish_deleted_translations:
            self.assertIsNotNone(translation.deleted_at)
