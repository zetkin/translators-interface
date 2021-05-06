from django.test import TestCase
import logging
from translations.models import Translation, Language, Project
from translations.utils.sync_project import sync_project


class SyncTestCase(TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

        english = Language.objects.create(name="English", language_code="en")
        swedish = Language.objects.create(name="Swedish", language_code="sv")

        self.project = Project.objects.create(
            name="Test Git Project",
            repository_name="zetkin/translators-interface",
            locale_files_path="backend/translations/utils/tests/mock_locale_files",
        )
        self.project.languages.add(english)
        self.project.languages.add(swedish)
        self.project.save()

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
