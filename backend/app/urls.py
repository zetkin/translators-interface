from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from translations.views.project import ProjectViewSet

router = routers.DefaultRouter()

# Rest Framework Viewsets
router.register(r"projects", ProjectViewSet, basename="projects")

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
