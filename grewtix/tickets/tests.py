from django.test import TestCase, Client
from .models import Ticket, TicketType, Project, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from model_bakery import baker
from django.urls import reverse
from datetime import timedelta
from django.utils import timezone

user_test_password = '12345'


##############################
#Create test case for:
#create ticket from POST request
#edit from EDIT request
#delete from request
#########################


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
    return x

def create_comment_attached_to_ticket(ticket):
    comment = baker.make("Comment")
    comment.ticketID = ticket
    comment.save()
    return comment

def update_tickets_creation_date(ticket, days):
    ticket.created_at = timezone.now() - timedelta(days=days)
    ticket.save()
    return ticket

def output_response(response):
    obj = response
    for attr in dir(obj):
        print("obj.%s = %r" % (attr, getattr(obj, attr)))

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

    def test_tickets_age(self):
        ticket = baker.make("Ticket")
        ticket.save()
        response = self.client.get(reverse('tickets:all_ticket_queue'))
        self.assertContains(response, "today.")                         #test that the ticket was created today.
        update_tickets_creation_date(ticket, 1)
        response = self.client.get(reverse('tickets:all_ticket_queue'))
        self.assertContains(response, "day ago.")                       #test that the ticket was created 1 day ago.
        update_tickets_creation_date(ticket, 2)
        response = self.client.get(reverse('tickets:all_ticket_queue'))
        self.assertContains(response, "days ago.")                      #test that the ticket was created 2 days ago.
        update_tickets_creation_date(ticket, -1)
        response = self.client.get(reverse('tickets:all_ticket_queue'))
        self.assertContains(response, """<ul class="list-group">""")    #test that the ticket was created 1 day in the future. Expected result is no tickets,
                                                                        #so check that the list group is created but empty.

    def test_assign_button(self):
        owner = create_user('testOwner')
        creator = create_user('testCreator')
        x = create_ticket('test ticket', creator, creator) 
        self.client.login(username='testOwner', password=user_test_password)            #Login as testowner
        response = self.client.get(reverse('tickets:owned_by_user_queue'))
        self.assertContains(response, 'No tickets are available')

        response = self.client.get(reverse('tickets:assign', kwargs={'ticket_id': x.id}))  #Check that the assign/ticket.id redirects to the edit page
        self.assertEqual(response.status_code, 302)
        
        response = self.client.get(reverse('tickets:owned_by_user_queue'))              #check that the assign user worked correctly
        self.assertContains(response, 'testOwner')

    def test_regex_edit_ticket_path(self):                                              #test that the reged path for tickets (ex. '\edit\prod-21')
        response = self.client.get('/edit/test-1234')                                   #expected output should be a redirect to 'edit\21' if the ticket
        self.assertContains(response, "Could not find the ticket you are looking for.") #exists.
        ticket = baker.make("Ticket")
        ticket.save()
        response = self.client.get('/edit/' + str(ticket))
        self.assertEqual(response.status_code, 302)
        

class test_ticket_model(TestCase):
    
    def test_get_comments(self):
        ticket = baker.make("Ticket")
        ticket.save()
        self.assertIs(ticket.get_comments(), None)          #Test without a comment, expected result is None
        comment = create_comment_attached_to_ticket(ticket)
        self.assertTrue(comment in ticket.get_comments())   #Test with a comment, expected result is comment to be returned in queryset
        response = Client().get(reverse('tickets:edit', kwargs={'pk': ticket.id}))
        self.assertContains(response, comment.comment)      #Test that the comment appears in the ticket edit page.

class test_ticket_querysets_view(TestCase):

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

        # obj = response
        # for attr in dir(obj):
        #     print("obj.%s = %r" % (attr, getattr(obj, attr)))