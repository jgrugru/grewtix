from django.test import TestCase
from model_bakery import baker
from tickets.models import Ticket, TicketType, Project  # flake8: F401


class TicketModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        ticket = baker.make(
            'Ticket',
            ticketType=baker.make('TicketType'),
            subject="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            project=baker.make('Project'),
            description="THIS IS A TEST 1.",
            priority='Low',
            status="Backlog",
            creator=baker.make('User'),
            owner=baker.make('User'),
        )
        ticket.save()

    def get_test_ticket(self):
        return Ticket.objects.get(id=1)

    def test_ticket_type_label(self):
        field_label = self.get_test_ticket()._meta.get_field('ticketType').verbose_name
        self.assertEqual(field_label, 'ticketType')

    def test_subject_label(self):
        field_label = self.get_test_ticket()._meta.get_field('subject').verbose_name
        self.assertEqual(field_label, 'subject')

    def test_subject_max_length(self):
        max_length = self.get_test_ticket()._meta.get_field('subject').max_length
        self.assertEqual(max_length, 75)

    def test_project_label(self):
        field_label = self.get_test_ticket()._meta.get_field('project').verbose_name
        self.assertEqual(field_label, 'project')

    def test_description_label(self):
        field_label = self.get_test_ticket()._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_max_length(self):
        max_length = self.get_test_ticket()._meta.get_field('description').max_length
        self.assertEqual(max_length, 1000)

    def test_priority_label(self):
        field_label = self.get_test_ticket()._meta.get_field('priority').verbose_name
        self.assertEqual(field_label, 'priority')

    def test_priority_max_length(self):
        max_length = self.get_test_ticket()._meta.get_field('priority').max_length
        self.assertEqual(max_length, 10)

    def test_status_label(self):
        field_label = self.get_test_ticket()._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')

    def test_status_max_length(self):
        max_length = self.get_test_ticket()._meta.get_field('status').max_length
        self.assertEqual(max_length, 40)

    def test_creator_label(self):
        field_label = self.get_test_ticket()._meta.get_field('creator').verbose_name
        self.assertEqual(field_label, 'creator')

    def test_owner_label(self):
        field_label = self.get_test_ticket()._meta.get_field('owner').verbose_name
        self.assertEqual(field_label, 'owner')

    def test_shortened_subject_str(self):
        self.assertEqual(self.get_test_ticket().shortened_subject_str(), 'ABCDEFGHIJKLMNOPQRST')

    def test_how_many_days_old(self):
        self.assertEqual(self.get_test_ticket().how_many_days_old(), 0)

    def test_get_absolute_url(self):
        self.assertEqual(self.get_test_ticket().get_absolute_url(), '/tickets/detail/1')

    def test_ticket_str(self):
        test_ticket = self.get_test_ticket()
        expected_str = f"{test_ticket.ticketType}-{test_ticket.id}"
        self.assertEqual(str(self.get_test_ticket()), expected_str)


class TicketTypeModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        ticket_type = baker.make(
            'TicketType',
            ticketType="DEV",
        )
        ticket_type.save()

    def get_test_ticket_type(self):
        return TicketType.objects.get(id=1)

    def test_ticket_type_label(self):
        field_label = self.get_test_ticket_type()._meta.get_field('ticketType').verbose_name
        self.assertEqual(field_label, 'ticketType')

    def test_ticket_type_max_length(self):
        max_length = self.get_test_ticket_type()._meta.get_field('ticketType').max_length
        self.assertEqual(max_length, 5)

    def test_ticket_type_str(self):
        self.assertEqual(str(self.get_test_ticket_type()), "DEV")


class ProjectModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        project = baker.make(
            'Project',
            project="TeamCity Upgrade",
        )
        project.save()

    def get_test_project(self):
        return Project.objects.get(id=1)

    def test_project_label(self):
        field_label = self.get_test_project()._meta.get_field('project').verbose_name
        self.assertEqual(field_label, 'project')

    def test_project_max_length(self):
        max_length = self.get_test_project()._meta.get_field('project').max_length
        self.assertEqual(max_length, 20)

    def test_project_str(self):
        self.assertEqual(str(self.get_test_project()), "TeamCity Upgrade")
