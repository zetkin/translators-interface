from django.test import TestCase
import logging
from translations.models import Translation, Language, Project
from translations.models.factories import (
    TranslationFactory,
    ProjectFactory,
    LanguageFactory,
)
from translations.utils.create_pr import create_pr


class SyncTestCase(TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

        english = LanguageFactory(name="English", language_code="en")
        swedish = LanguageFactory(name="Swedish", language_code="sv")

        self.project = ProjectFactory(
            name="Test Git Project",
            repository_name="zetkin/translators-interface",
            locale_files_path="backend/translations/utils/tests/mock_locale_files",
            languages=(english, swedish),
        )

        # Create translations for language

    def test_create_pr(self):
        create_pr(self.project)

        self.assertEqual(0, 1)
