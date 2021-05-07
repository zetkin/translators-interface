from rest_framework import viewsets

from translations.models import Translation, TranslationSerializer


class TranslationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows list, retrieve, and
    create actions for the Translation model.
    """

    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
