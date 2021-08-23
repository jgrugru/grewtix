from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TicketType(TimeStampMixin):  # 1 to many
    ticketType = models.CharField(max_length=5)

    def __str__(self):
        return self.ticketType


class Project(TimeStampMixin):  # 1 to many
    project = models.CharField(max_length=20)

    def __str__(self):
        return self.project


class Ticket(TimeStampMixin):

    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    )

    STATUS_CHOICES = (
        ('Backlog', 'Backlog'),
        ('Waiting On Submitter', 'Waiting On Submitter'),
        ('In Progress', 'In Progress'),
        ('Waiting On Support', 'Waiting On Support'),
    )

    ticketType = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    subject = models.CharField(max_length=75)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, default='')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, blank=True)
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, blank=True)
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('tickets:ticket_detail', args=[str(self.id)])

    def how_many_days_old(self):
        delta = timezone.now() - self.created_at
        return delta.days

    def shortened_subject_str(self):
        return self.subject[0:20]

    def __str__(self):
        return self.ticketType.ticketType + '-' + str(self.id)
