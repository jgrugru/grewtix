from django.test import TestCase
from .models import Ticket, TicketType, Project
from django.contrib.auth.models import User
from model_bakery import baker

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

    
def create_ticket():
    x = baker.make('Ticket')
    print(x.ticketType, x.subject, x.project, x.description, x.priority, x.status, x.creator, x.owner)
    x = Ticket(ticketType=create_ticketType(), subject='test', project=create_project(), description='testing', priority='Critical', status='Backlog', creator=create_user())
    print(x.ticketType, x.subject, x.project, x.description, x.priority, x.status, x.creator, x.owner)

    return x
 

class TicketModelTests(TestCase):

    def test_Baker(self):
        print(type(create_ticketType()))
        print(type(create_project()))
        print(type(create_ticket()))
