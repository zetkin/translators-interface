from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend

from translations.models import Translation, TranslationSerializer


class TranslationViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows list, retrieve, and create actions for the Translation model.
    """

    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["language", "project", "from_repository"]
