from django.core.management.base import BaseCommand
from model_bakery import baker
from tickets.models import Project  # noqa: F401


class Command(BaseCommand):
    help = 'Pass an integer, how many mock projects you want created'

    def add_arguments(self, parser):
        parser.add_argument('populate', type=int)

    def handle(self, *args, **options):
        if options['populate']:
            for count in range(int(options['populate'])):
                project = baker.make('Project')
                print("Created: " + str(project))
                project.save()
