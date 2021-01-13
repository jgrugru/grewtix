from django.test import TestCase, Client
from .models import Ticket, TicketType, Project
from django.contrib.auth.models import User
from model_bakery import baker
from django.urls import reverse

# Create your tests here.
def create_ticketType():
    x =  baker.make('TicketType')
    return x

def create_project():
    x =  baker.make('Project')
    return x

def create_user():
    x = baker.make('User')
    return x

# class TicketModelTests(TestCase):

#     def create_ticket(self):
#         x = baker.make('Ticket')
#         # print(x.ticketType, x.subject, x.project, x.description, x.priority, x.status, x.creator, x.owner)
#         return x
 
#     def test_Baker(self):
#         print(type(create_ticketType()))
#         print(type(create_project()))
#         print(type('ticket: ', self.create_ticket()))

class TicketIndexViewTests(TestCase):
    def test_no_tickets(self):
        response = self.client.get(reverse('tickets:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_ticket_list'], [])
