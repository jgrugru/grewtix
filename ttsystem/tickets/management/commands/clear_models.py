from django.core.management.base import BaseCommand
from tickets.models import TicketType, Project, Priority, Status, Ticket, Attachment, Comment

class Command(BaseCommand):
    def handle(self, *args, **options):
        # TicketType.objects.all().delete()
        # Project.objects.all().delete()
        # Priority.objects.all().delete()
        # Status.objects.all().delete()
        Ticket.objects.all().delete()
        # Attachment.objects.all().delete()
        # Comment.objects.all().delete()