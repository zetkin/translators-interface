import factory
from factory import fuzzy
from translations.models import Translation, Project, Language

# https://factoryboy.readthedocs.io/en/stable/recipes.html#simple-many-to-many-relationship


class LanguageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Language

    name = fuzzy.FuzzyText()
    language_code = fuzzy.FuzzyText(length=2)


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    name = fuzzy.FuzzyText()
    repository_name = fuzzy.FuzzyText()
    locale_files_path = fuzzy.FuzzyText()

    # Project factory requires languages passed in when created
    @factory.post_generation
    def languages(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            # A list of languages were passed in, use them
            for language in extracted:
                self.languages.add(language)


class TranslationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Translation

    text = fuzzy.FuzzyText()
    author = fuzzy.FuzzyText()
    from_repository = False
    file_path = fuzzy.FuzzyText()
    object_path = fuzzy.FuzzyText()
    project = factory.Iterator(Project.objects.all())
    language = factory.Iterator(Language.objects.all())
