from translations.models import Project, Language


def filter_latest_translations(translations_qs):

    translations_hashmap = {}

    # Get all values of projects in queryset
    unique_project_ids = set(
        translations_qs.values_list("project", flat=True).distinct()
    )
    projects = Project.objects.filter(id__in=unique_project_ids)

    for project in projects:
        # Add projects to hashmap
        translations_hashmap[project.id] = {}

        # Get languages for the project
        languages = project.languages.all()

        for language in languages:
            # Add language to hashmap
            translations_hashmap[project.id][language.language_code] = {}

            # Get translations for project and language
            translations = translations_qs.filter(project=project, language=language)

            for translation in translations:
                # If translation not yet in hashmap
                dotpath = translation.dotpath
                current_translation_value = translations_hashmap[project.id][
                    language.language_code
                ].get(translation.dotpath)

                if not current_translation_value:
                    # Add it
                    translations_hashmap[project.id][language.language_code][
                        translation.dotpath
                    ] = translation

                if current_translation_value:
                    # Replace if translation in hashmap is older than current translation
                    if current_translation_value.created_at < translation.created_at:
                        translations_hashmap[project.id][language.language_code][
                            translation.dotpath
                        ] = translation

    # Get translations out of hashmap
    latest_translation_ids = []
    for project_id in translations_hashmap:
        for language_id in translations_hashmap[project_id]:
            for translation_key in translations_hashmap[project_id][language_id]:
                latest_translation_ids.append(
                    translations_hashmap[project_id][language_id][translation_key].id
                )

    return translations_qs.filter(id__in=latest_translation_ids)
