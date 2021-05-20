from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend

from translations.models import Translation, TranslationSerializer, Project, Language
from translations.utils.filter_latest_translations import filter_latest_translations


class TranslationViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows list, retrieve, and create actions for the Translation model.

    Supports filtering on the language, project, and from_repository.

    By default, the list function only returns the most recent translation for a dotpath, but the queryparam "history" can be set to true, which returns all translations.
    """

    queryset = Translation.objects.order_by("-created_at")
    serializer_class = TranslationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["language", "project", "from_repository"]
    pagination_class = None

    def list(self, request, *args, **kwargs):
        # Return only latest translations if the queryparam "history" not set to true
        if not request.query_params.get("history"):
            self.queryset = filter_latest_translations(self.get_queryset())
        return super().list(request, *args, **kwargs)
