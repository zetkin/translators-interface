from datetime import datetime
from typing import Dict
from django.db.models.query import QuerySet
from translations.models.translation import Translation


def mark_deleted_translations(
    previous_translations: QuerySet[Translation],
    all_translations_in_project: Dict[str, Dict[str, Translation]],
    sync_time: datetime,
):
    for translation in previous_translations:
        # If previous translation not in the current translations
        if (
            translation.file_path not in all_translations_in_project
            or translation.object_path
            not in all_translations_in_project[translation.file_path]
        ):
            # Mark all translations from previous translation as deleted
            deleted_translations = Translation.objects.filter(
                file_path=translation.file_path, object_path=translation.object_path
            )
            for deleted_translation in deleted_translations:
                deleted_translation.deleted_at = sync_time
                deleted_translation.save()
