from django.test import TestCase
from django.utils.timezone import now
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


class GenerateLocalFilesTestCase(TestCase):
    path = os.path.join(os.getcwd(), "translations/utils/tests/mock_generated_files")

    def setUp(self):
        logging.disable(logging.CRITICAL)

        self.english = LanguageFactory(name="English", language_code="en")
        self.swedish = LanguageFactory(name="Swedish", language_code="sv")

        self.project = ProjectFactory(
            name="Test Git Project",
            repository_name="zetkin/translators-interface",
            locale_files_path="backend/translations/utils/tests/mock_files/sync_project",
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
                
        Deletions
            Deleted translation at `home.content.p` 
                - Both English and Swedish. 
                - These translations should not be generated
        """
        TranslationFactory(
            file_path="./en.yaml", object_path="author", language=self.english
        )
        TranslationFactory(
            file_path="./sv.yaml", object_path="author", language=self.swedish
        )

        TranslationFactory(
            file_path="./home/en.yaml", object_path="title", language=self.english
        )
        TranslationFactory(
            file_path="./home/en.yaml",
            object_path="content.header",
            language=self.english,
        )
        TranslationFactory(
            file_path="./home/en.yaml",
            object_path="content.subheader",
            language=self.english,
        )

        TranslationFactory(
            file_path="./home/sv.yaml", object_path="title", language=self.swedish
        )
        TranslationFactory(
            file_path="./home/sv.yaml",
            object_path="content.header",
            language=self.swedish,
        )

        # Deleted Translations
        TranslationFactory(
            file_path="./home/en.yaml",
            object_path="content.p",
            language=self.english,
            deleted_at=now(),
        )
        TranslationFactory(
            file_path="./home/sv.yaml",
            object_path="content.p",
            language=self.swedish,
            deleted_at=now(),
        )

        # Delete folder before each test
        if os.path.isdir(self.path):
            shutil.rmtree(self.path)

        # Make folder to generate in
        os.makedirs(self.path)

    @classmethod
    def tearDownClass(cls) -> None:
        # Delete folder after all tests finish
        shutil.rmtree(cls.path)
        return super().tearDownClass()

    def test_generate_locale_files(self):
        # Generates files with correct contents within the mock_generated_files folder
        generate_locale_files(self.project, self.path)

        for t in Translation.objects.all():
            # Get contents of file translation should be in
            file_path = os.path.join(self.path, "/".join(t.file_path.split("/")[1:]))
            with open(file_path, "r") as f:
                yaml_contents = yaml.load(f, Loader=Loader)
                flat_file_object = json_normalize(yaml_contents, sep=".").to_dict(
                    orient="records"
                )[0]
                # If translation has not been deleted
                if not t.deleted_at:
                    # Check that the YAML file contains the selected translation at the correct object path
                    self.assertEqual(flat_file_object[t.object_path], t.text)
                else:  # Translation has been deleted
                    # Check it does not exist in file
                    self.assertTrue(t.object_path not in flat_file_object)

    def test_yaml_indentation(self):
        # Set indentation for 4
        self.project.yaml_indentation = 4
        self.project.save()

        # Generates files with correct contents within the mock_generated_files folder
        generate_locale_files(self.project, self.path)

        # Open home/en.yaml and check the indentation of 'content.subheader'
        home_content_translation = Translation.objects.get(
            file_path="./home/en.yaml",
            object_path="content.subheader",
            language=self.english,
        )
        file_path = os.path.join(
            self.path, "/".join(home_content_translation.file_path.split("/")[1:])
        )
        with open(file_path, "r") as f:
            for line in f:
                if "subheader" in line:
                    # First 4 characters are spaces
                    self.assertEqual(line[:4], "    ")
