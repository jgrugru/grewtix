from django.test import TestCase
from model_bakery import baker
from django.urls import reverse
from django.contrib.auth.models import User


class TicketViewTestCRUD(TestCase):
    @classmethod  # ran once at beginning of testing.
    def setUpTestData(cls):
        baker.make('User')  # make a user with the id of 1; will be used to login
        number_of_tickets = 11
        baker.make(
            'Ticket',
            ticketType=baker.make('TicketType'),
            project=baker.make('Project'),
            subject="TEST 1",
            description="THIS IS A TEST 1.",
            priority='Low',
            status="Backlog",
            creator=baker.make('User'),
        )

        for x in range(number_of_tickets):
            baker.make('Ticket')

    def setUp(self):
        self.login()

    def login(self):
        self.client.force_login(User.objects.get(id=1))

    def test_ticket_edit_view(self):
        self.login()
        response = self.client.get(reverse('tickets:ticket_detail', kwargs={'pk': 1}))
        print(response)
