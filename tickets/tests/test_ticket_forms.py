from django import test
from django.test import TestCase
from model_bakery import baker

from tickets.models import Ticket
from tickets.forms import TicketForm


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

    def get_test_ticket(self):
        return Ticket.objects.get(id=1)

    # def setUp(self):  # this is called for every function
    #     ticket = baker.make(
    #         'Ticket',
    #         ticketType=baker.make('TicketType'),
    #         subject="TEST 2",
    #         project=baker.make('Project'),
    #         description="THIS IS A TEST 2.",
    #         priority='Low',
    #         status="Backlog",
    #         creator=baker.make('User'),
    #     )
    #     ticket.save()

    def test_ticket_form(self):
        testTicket = self.get_test_ticket()
        data={
            'ticketType': testTicket.ticketType,
            'subject': testTicket.subject,
            'project': testTicket.project,
            'description': testTicket.description,
            'priority': testTicket.priority,
            'status': testTicket.status,
            'creator': testTicket.creator,
            'owner': testTicket.owner
        }
        form = TicketForm(data)

        # print(form.is_valid(), "***********")
        self.assertTrue(form.is_valid())