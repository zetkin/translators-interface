from django.core.management.base import BaseCommand, CommandError
from translations.models import Project
from translations.utils.sync_project import sync_project


class Command(BaseCommand):
    help = "Trigger a project to sync all translations"

    def add_arguments(self, parser):
        parser.add_argument("project", type=str)

    def handle(self, *args, **options):
        try:
            project = Project.objects.get(name=options["project"])
            sync_project(project)
            self.stdout.write(
                self.style.SUCCESS('Successfully synced project "%s"' % project.name)
            )

        except Project.DoesNotExist:
            raise CommandError('Project "%s" does not exist' % options.project)
