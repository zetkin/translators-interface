from django.test import TestCase
import os, logging, shutil, yaml
from pandas import json_normalize
from yaml import Loader

from translations.models import Translation
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
        path = os.path.join(
            os.getcwd(), "translations/utils/tests/mock_generated_files", ""
        )

        # If cleanup failed, delete folder
        if os.path.isdir(path):
            shutil.rmtree(path)

        # Make folder to generate in
        os.makedirs(path)

        # Generates files with correct contents within the mock_generated_files folder
        generate_locale_files(self.project, path)

        for t in Translation.objects.all():
            # Get contents of file translation should be in
            file_path = os.path.join(path, "/".join(t.file_path.split("/")[1:]))
            with open(file_path, "r") as f:
                yaml_contents = yaml.load(f, Loader=Loader)
                flat_file_object = json_normalize(yaml_contents, sep=".").to_dict(
                    orient="records"
                )[0]
                # Check that the YAML file contains the selected translation at the correct object path
                self.assertEqual(flat_file_object[t.object_path], t.text)

        # Clean up
        shutil.rmtree(path)
