from django.test import TestCase
from django.utils.timezone import now

from translations.models import Translation
from translations.models.factories import (
    LanguageFactory,
    ProjectFactory,
    LanguageFactory,
    TranslationFactory,
)
from translations.utils.mark_deleted_translations import mark_deleted_translations


class MarkDeletedTranslations(TestCase):
    def setUp(self):
        english = LanguageFactory(name="English", language_code="en")
        project = ProjectFactory(
            name="Test Git Project",
            repository_name="zetkin/translators-interface",
            locale_files_path="backend/translations/utils/tests/mock_files/sync_project",
            languages=(english,),
        )

        """
          Translation record, 5 of every translation

            ./home/en.yaml
              h1
            ./home/content/en.yaml
              section.h1
              section.p
        """
        TranslationFactory.create_batch(
            5,
            file_path="./home/en.yaml",
            object_path="h1",
            language=english,
            project=project,
        )
        TranslationFactory.create_batch(
            5,
            file_path="./home/content/en.yaml",
            object_path="section.p",
            language=english,
            project=project,
        )
        # This translation will be deleted
        TranslationFactory.create_batch(
            5,
            file_path="./home/content/en.yaml",
            object_path="section.h1",
            language=english,
            project=project,
        )

    def test_mark_deleted_translations(self):
        home_h1 = Translation.objects.filter(
            file_path="./home/en.yaml", object_path="h1"
        )[0]
        home_content_section_p = Translation.objects.filter(
            file_path="./home/content/en.yaml", object_path="section.p"
        )[0]
        all_translations_in_project = {
            "./home/en.yaml": {"h1": home_h1},
            "./home/content/en.yaml": {"section.p": home_content_section_p},
        }

        mark_deleted_translations(
            Translation.objects.all(), all_translations_in_project, sync_time=now()
        )

        # Deleted Translations
        deleted_translations = Translation.objects.filter(
            file_path="./home/content/en.yaml", object_path="section.h1"
        )
        self.assertEqual(deleted_translations.count(), 5)
        for translation in deleted_translations:
            self.assertIsNotNone(translation.deleted_at)
        # Non deleted translations
        non_deleted_translations = Translation.objects.exclude(deleted_at__isnull=False)
        for translation in non_deleted_translations:
            self.assertIsNone(translation.deleted_at)
