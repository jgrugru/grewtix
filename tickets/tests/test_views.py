from django.test import TestCase
from model_bakery import baker
from django.contrib.auth.models import User
from tickets.models import Ticket, TicketType, Project  #flake8: F401

class AnimalTestCase(TestCase):
    def setUp(self):
        ticket = baker.make(
            'Ticket',
            ticketType=baker.make('TicketType'),
            project=baker.make('Project'),
            description="THIS IS A TEST.",
            priority='Low',
            status="Backlog",
            creator=baker.make('User'),
        )
        ticket.save()

    def test_get_absolute_url(self):
        author = Ticket.objects.get(id=1)
        self.assertEqual(author.get_absolute_url(), '/tickets/detail/1')