from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend

from translations.models import Translation, TranslationSerializer, Project, Language


class TranslationViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows list, retrieve, and create actions for the Translation model.

    Supports filtering on the language, project, and from_repository. Also accept query parameter "latest" which takes a boolean, and if true it only returns one of each
    """

    queryset = Translation.objects.order_by("-created_at")
    serializer_class = TranslationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["language", "project", "from_repository"]

    # Overwrite list default
    def list(self, request, *args, **kwargs):
        if not request.query_params.get("latest"):
            # If no param latest, return all translations
            return super().list(request, *args, **kwargs)
        else:
            """
            Hashmap of:
                project_id
                    language_code
                        dotpath
            """
            qs = self.get_queryset()
            translations_hashmap = {}

            # Get all values of projects in queryset
            unique_project_ids = set(qs.values_list("project", flat=True).distinct())
            projects = Project.objects.filter(id__in=unique_project_ids)

            for project in projects:
                # Add projects to hashmap
                translations_hashmap[project.id] = {}

                # Get languages for the project
                languages = project.languages.all()

                for language in languages:
                    # Add language to hashmap
                    translations_hashmap[project.id][language.language_code] = {}

                    # Get translations for project and language
                    translations = qs.filter(project=project, language=language)

                    for translation in translations:
                        # If translation not yet in hashmap
                        dotpath = translation.dotpath
                        current_translation_value = translations_hashmap[project.id][
                            language.language_code
                        ].get(translation.dotpath)

                        if not current_translation_value:
                            # Add it
                            translations_hashmap[project.id][language.language_code][
                                translation.dotpath
                            ] = translation

                        if current_translation_value:
                            # Replace if translation in hashmap is older than current translation
                            if (
                                current_translation_value.created_at
                                < translation.created_at
                            ):
                                translations_hashmap[project.id][
                                    language.language_code
                                ][translation.dotpath] = translation

            # Get translations out of hashmap
            latest_translation_ids = []
            for project_id in translations_hashmap:
                for language_id in translations_hashmap[project_id]:
                    for translation_key in translations_hashmap[project_id][
                        language_id
                    ]:
                        latest_translation_ids.append(
                            translations_hashmap[project_id][language_id][
                                translation_key
                            ].id
                        )

            self.queryset = qs.filter(id__in=latest_translation_ids)

            return super().list(request, *args, **kwargs)
