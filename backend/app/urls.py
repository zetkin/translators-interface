from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from translations.views.project import ProjectViewSet
from translations.views.translation import TranslationViewSet

router = routers.DefaultRouter()

# Rest Framework Viewsets
router.register(r"projects", ProjectViewSet, basename="projects")
router.register(r"translations", TranslationViewSet, basename="translations")


urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
