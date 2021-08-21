from django.core.management.base import BaseCommand
from tickets.models import Ticket

class Command(BaseCommand):
    help = '-p: print all the tickets | ' + \
            '-d: delete all the tickets | ' + \
            '--populate: add test ticket data'

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            action='store_true',
            help="Print all the current tickets.",
        )
        parser.add_argument(
            '--delete',
            action='store_true',
            help="Delete all the current tickets.",
        )

    def delete_tickets():
        print("Deleting all tickets")
        for ticket in Ticket.objects.all():
            print("Deleting " + str(ticket))
            ticket.delete()

    def handle(self, *args, **options):
        if options['p']:
            print(Ticket.objects.all())
        
        if options['delete']:
            self.delete_tickets()