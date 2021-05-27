from django.test import TestCase
import os, glob, logging
from translations.models import Translation, Language, Project
from translations.models.factories import (
    LanguageFactory,
    ProjectFactory,
    LanguageFactory,
    TranslationFactory,
)
from translations.utils.generate_locale_files import generate_locale_files
from translations.utils.sync_project import sync_project


class SyncTestCase(TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

        self.english = LanguageFactory(name="English", language_code="en")
        self.swedish = LanguageFactory(name="Swedish", language_code="sv")

        self.project = ProjectFactory(
            name="Test Git Project",
            repository_name="zetkin/translators-interface",
            locale_files_path="backend/translations/utils/tests/mock_locale_files",
            languages=(self.english, self.swedish),
        )

        """
        Translations recreating this folder structure

            en.yaml
                author
            sv.yaml
                author
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
        TranslationFactory(file_path="./en.yaml", object_path="author")
        TranslationFactory(file_path="./sv.yaml", object_path="author")

        TranslationFactory(file_path="./home/en.yaml", object_path="title")
        TranslationFactory(file_path="./home/en.yaml", object_path="content.header")
        TranslationFactory(file_path="./home/en.yaml", object_path="content.subheader")

        TranslationFactory(file_path="./home/sv.yaml", object_path="title")
        TranslationFactory(file_path="./home/sv.yaml", object_path="content.header")

    def test_generate_locale_files(self):
        # Generates files with correct contents within the mock_generated_files folder
        path = os.path.join(
            os.getcwd(), "translations/utils/tests/mock_generated_files"
        )
        generate_locale_files(self.project, path)

        # Delete all contents of generated files
        # filelist = glob.glob(os.path.join(path, "*"))
        # for f in filelist:
        #     os.remove(f)

        self.assertEqual(0, 1)
