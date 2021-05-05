from django.test import TestCase
from translations.models import Translation, Language, Project


class SyncTestCase(TestCase):
    def setUp(self):
        english = Language.objects.create(name="English", language_code="en")
        swedish = Language.objects.create(name="Swedish", language_code="se")

        project = Project.objects.create(
            name="Test Git Project",
            repository_url="https://github.com/zetkin/translators-interface",
            locale_files_path="./backend/translations/tests/mock_locale",
        )
        project.languages.add(english)
        project.languages.add(swedish)
        project.save()

    def test_create_translations_from_git(self):
        pass
