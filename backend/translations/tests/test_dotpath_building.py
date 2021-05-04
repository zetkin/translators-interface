from django.test import TestCase
from translations.models import Translation, Language, Project

# Test that dotpath is correctly generated for a translation
class DotpathBuildingTestCase(TestCase):
    def setUp(self):
        language = Language.objects.create(name="Dutch", language_code="nl")
        project = Project.objects.create(name="Seinfeld Season 1")
        project.languages.add(language)
        project.save()

        self.translation = Translation.objects.create(
            text="Example text",
            author="Martin van Nostrand",
            from_repository=True,
            file_path=".",
            object_path="exampleKey",
            project=project,
            language=language,
        )

    def test_root_path_single_nested_key(self):
        self.assertEqual(self.translation.dotpath, "exampleKey")
