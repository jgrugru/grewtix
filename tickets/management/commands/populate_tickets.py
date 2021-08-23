from django.core.management.base import BaseCommand
from model_bakery import baker
from tickets.models import Ticket, TicketType, Project  # noqa: F401
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Pass an integer, how many mock tickets you want created'

    def add_arguments(self, parser):
        parser.add_argument('populate', type=int)

    def handle(self, *args, **options):
        if options['populate']:
            for count in range(int(options['populate'])):
                ticket = baker.make(
                    'Ticket',
                    ticketType=TicketType.objects.all()[0],
                    project=Project.objects.all()[0],
                    description="THIS IS A TEST.",
                    priority='Low',
                    status="Backlog",
                    creator=User.objects.filter(username="jgruenbaum")[0],
                )
                print("Created: " + str(ticket))
                ticket.save()
