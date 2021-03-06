from django.core.management.base import BaseCommand, CommandError
from translations.models import Project
from translations.utils.create_pr import create_pr


class Command(BaseCommand):
    help = "Make a pull request "

    def add_arguments(self, parser):
        parser.add_argument("project", type=str)

    def handle(self, *args, **options):
        try:
            project = Project.objects.get(name=options["project"])

            create_pr(project)

            self.stdout.write(
                self.style.SUCCESS(
                    'Pull request made for translation in project "%s"' % project.name
                )
            )

        except Project.DoesNotExist:
            raise CommandError('Project "%s" does not exist' % options.project)
