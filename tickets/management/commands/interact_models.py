from django.core.management.base import BaseCommand
from tickets.models import TicketType, Ticket, Project
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = '-p: print all the tickets | ' + \
            '-d: delete all the tickets | '

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            action='store_true',
            help="Print all the current tickets.",
        )
        parser.add_argument(
            '--deletetickettypes',
            action='store_true',
            help="Delete all the ticket types.",
        )
        parser.add_argument(
            '--deletetickets',
            action='store_true',
            help="Delete all the current tickets.",
        )
        parser.add_argument(
            '--deleteprojects',
            action='store_true',
            help="Delete all the current projects.",
        )
        parser.add_argument(
            '--deleteusers',
            action='store_true',
            help="Delete all the current users with names longer than 20 chars.",
        )
        parser.add_argument(
            '--totaldelete',
            action='store_true',
            help="Delete all the current users, projects, tickettypes.",
        )

    def delete_tickettypes(self):
        print("Deleting all ticket types.")
        for tickettype in TicketType.objects.all():
            print("Deleting " + str(tickettype))
            tickettype.delete()

    def delete_tickets(self):
        print("Deleting all tickets.")
        for ticket in Ticket.objects.all():
            print("Deleting " + str(ticket))
            ticket.delete()

    def delete_projects(self):
        print("Deleting all projects.")
        for project in Project.objects.all():
            print("Deleting " + str(project))
            project.delete()

    def delete_users(self):
        print("Deleting all users with len(username) > 20.")
        for user in User.objects.all():
            if len(user.username) > 20:
                print("Deleting " + str(user))
                user.delete()

    def handle(self, *args, **options):
        if options['p']:
            print(Ticket.objects.all())

        if options['deletetickettypes']:
            self.delete_tickettypes()

        if options['deletetickets']:
            self.delete_tickets()

        if options['deleteprojects']:
            self.delete_projects()

        if options['deleteusers']:
            self.delete_users()

        if options['totaldelete']:
            self.delete_projects()
            self.delete_tickets()
            self.delete_users()
            self.delete_tickettypes()
