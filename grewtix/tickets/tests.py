from django.test import TestCase, Client
from .models import Ticket, TicketType, Project, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from model_bakery import baker
from django.urls import reverse

user_test_password = '12345'

def create_user(username):
    user = User.objects.create(username=username)
    user.set_password(user_test_password)
    user.save()
    return user

def create_ticket(ticket_subject, owner, creator):
    x = baker.make('Ticket')
    x.owner = owner
    x.creator = creator
    x.subject = ticket_subject
    x.save()
    # print(x.subject, x.creator, x.owner, x.created_at)
    # print(x.ticketType, x.subject, x.project, x.description, x.priority, x.status, x.creator, x.owner)
    return x
 

class test_login(TestCase):

    def test_login(self):
        client = Client()
        user = create_user('testuser')
        self.assertTrue(client.login(username='testuser', password=user_test_password))

class test_features(TestCase):

    def test_index_response_code(self):
        response = self.client.get(reverse('tickets:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Unassigned Queue")

class test_ticket_model(TestCase):
    
    def test_get_comments(self):
        ticket = baker.make("Ticket")
        ticket.save()
        self.assertIs(ticket.get_comments(), None)          #Test without a comment, expected result is None
        comment = baker.make("Comment")
        comment.ticketID = ticket
        comment.save()
        self.assertTrue(comment in ticket.get_comments())   #Test with a comment, expected result is comment to be returned in queryset

class test_ticket_querysets(TestCase):

    def __init__(self, x):
        super().__init__(x)
        self.client = Client()
        
    def setup_with_ticket(self):
        owner = create_user('testOwner')
        creator = create_user('testCreator')
        x = create_ticket('test ticket', owner, creator) 
        self.client.login(username='testOwner', password=user_test_password)

    def setup_without_ticket(self):
        owner = create_user('testOwner')
        self.client.login(username='testOwner', password=user_test_password)

    def test_owned_by_user_queue_with_ticket(self):
        self.setup_with_ticket()
        response = self.client.get(reverse('tickets:owned_by_user_queue'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testOwner')

    def test_owned_by_user_queue_without_ticket(self):
        self.setup_without_ticket()
        response = self.client.get(reverse('tickets:owned_by_user_queue'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No tickets are available')

    def test_created_by_user_queue_with_ticket(self):
        self.setup_with_ticket()
        response = self.client.get(reverse('tickets:created_by_user_queue'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testOwner')

    def test_created_by_user_queue_without_ticket(self):
        self.setup_without_ticket()
        response = self.client.get(reverse('tickets:created_by_user_queue'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No tickets are available')

    def test_unassigned_queue_with_ticket(self):
        self.setup_with_ticket()
        response = self.client.get(reverse('tickets:unassigned_queue'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testOwner')

    def test_unassigned_queue_without_ticket(self):
        self.setup_without_ticket()
        response = self.client.get(reverse('tickets:unassigned_queue'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No tickets are available')

    def test_recently_created_queue_with_ticket(self):
        self.setup_with_ticket()
        response = self.client.get(reverse('tickets:recently_created_queue'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testOwner')

    def test_recently_created_queue_without_ticket(self):
        self.setup_without_ticket()
        response = self.client.get(reverse('tickets:recently_created_queue'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No tickets are available')
        
    def test_all_ticket_queue_with_ticket(self):
        self.setup_with_ticket()
        response = self.client.get(reverse('tickets:all_ticket_queue'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testOwner')

    def test_all_ticket_queue_without_ticket(self):
        self.setup_without_ticket()
        response = self.client.get(reverse('tickets:all_ticket_queue'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No tickets are available')


        # for z in Ticket.objects.all():
        #     print("****************&&&&&&&&&&&&&&$$$$$$$$$$$$$$$$$$", z.owner)
        #obj = response
        # for attr in dir(obj):
        #     print("obj.%s = %r" % (attr, getattr(obj, attr)))