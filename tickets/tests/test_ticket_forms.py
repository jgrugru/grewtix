from django.test import TestCase
from model_bakery import baker
from tickets.models import Ticket  # flake8: F401


class TicketFormTestCase(TestCase):
    @classmethod  # ran once at beginning of testing.
    def setUpTestData(cls):
        ticket = baker.make(
            'Ticket',
            ticketType=baker.make('TicketType'),
            project=baker.make('Project'),
            subject="TEST 1",
            description="THIS IS A TEST 1.",
            priority='Low',
            status="Backlog",
            creator=baker.make('User'),
        )
        ticket.save()

    def setUp(self):  # this is called for every function
        ticket = baker.make(
            'Ticket',
            ticketType=baker.make('TicketType'),
            subject="TEST 2",
            project=baker.make('Project'),
            description="THIS IS A TEST 2.",
            priority='Low',
            status="Backlog",
            creator=baker.make('User'),
        )
        ticket.save()

    def test_get_absolute_url(self):
        author = Ticket.objects.get(id=1)
        self.assertEqual(author.get_absolute_url(), '/tickets/detail/1')
