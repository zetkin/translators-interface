 from django.test import TestCase
import logging
from translations.models import Translation, Language, Project
from translations.models.factories import (
    TranslationFactory,
    ProjectFactory,
    LanguageFactory,
)
from translations.utils.sync_project import sync_project

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
        
        """
        Translations recreating this folder structure

            en.yaml
            sv.yaml
            home
                en.yaml
                    title
                    content
                        header
                        subheader
                sv.yaml
                    title
                    content
                        header
                        # NO SUBHEADER
                

        """

    def test_create_pr(self):
        # Create temp folder

        # Check that all files and contents exist in this folder

        self.assertEqual(0, 1)
