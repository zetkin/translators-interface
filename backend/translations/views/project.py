from rest_framework import viewsets, serializers

from translations.models import Project, Language


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = "__all__"


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows readonly methods for the Project model.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
