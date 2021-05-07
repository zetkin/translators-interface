from rest_framework import viewsets, serializers

from translations.models import Project, Language, Translation

# class TranslationSerializer(serializers.ModelSerializer):
#     Meta


class TranslationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows list, retrieve, and
    create actions for the Translation model.
    """

    queryset = Translation.objects.all()
    serializer_class = ProjectSerializer
