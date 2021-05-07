from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from translations.models import Translation, TranslationSerializer


class TranslationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows list, retrieve, and create actions for the Translation model.
    """

    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["language", "project", "dotpath", "from_repository"]
