from django.test import TestCase
from translations.models import Translation, Language, Project
from translations.models.factories import (
    TranslationFactory,
    LanguageFactory,
    ProjectFactory,
)

# Test that dotpath is correctly generated for a translation
class DotpathBuildingTestCase(TestCase):
    def setUp(self):
        dutch = LanguageFactory(name="Dutch", language_code="nl")
        project = ProjectFactory(name="Seinfeld Season 1", languages=[dutch])

        self.translation = TranslationFactory(
            text="I need to see Elaine Benes' chart.",
            author="Martin van Nostrand",
            from_repository=True,
            file_path="./nl.yaml",
            object_path="intro",
            project=project,
            language=dutch,
        )

    def test_root_path_single_nested_key(self):
        self.assertEqual(self.translation.dotpath, "intro")

    def test_single_folder_path_single_nested_key(self):
        self.translation.file_path = "./episode_1/nl.yaml"
        self.translation.save()
        self.assertEqual(self.translation.dotpath, "episode_1.intro")

    def test_multiple_folder_path_multiple_nested_key(self):
        self.translation.file_path = "./episode_1/part_1/nl.yaml"
        self.translation.object_path = "intro.header"
        self.translation.save()
        self.assertEqual(self.translation.dotpath, "episode_1.part_1.intro.header")
