from django.test import TestCase
from translations.models import Translation, Language, Project
from translations.sync import sync


class SyncTestCase(TestCase):
    def setUp(self):
        english = Language.objects.create(name="English", language_code="en")
        swedish = Language.objects.create(name="Swedish", language_code="se")

        self.project = Project.objects.create(
            name="Test Git Project",
            repository_url="https://github.com/zetkin/translators-interface",
            locale_files_path="./backend/translations/tests/mock_locale",
        )
        self.project.languages.add(english)
        self.project.languages.add(swedish)
        self.project.save()

    def test_create_translations_from_git(self):
        sync(self.project)
        self.assertEqual(1, 2)


# Should create english translations
