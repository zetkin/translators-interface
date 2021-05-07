from rest_framework import viewsets

from translations.models import Project, ProjectSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows readonly methods for the Project model.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
