from django.db import models
from django.utils import timezone, dateformat
from django.contrib.auth.models import User


# Create your models here.

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class TicketType(TimeStampMixin): #1 to many
    ticketType = models.CharField(max_length=5)
    
    def __str__(self):
        return self.ticketType

class Project(TimeStampMixin): #1 to many
    project = models.CharField(max_length=50)

    def __str__(self):
        return self.project

class Priority(TimeStampMixin): #1 to many
    priority = models.CharField(max_length=10)

    def __str__(self):
        return self.priority

class Status(TimeStampMixin): #1 to many
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status

class Ticket(TimeStampMixin):

    PRIORITY_CHOICES = ( 
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
        ('Critical','Critical'),
    )

    STATUS_CHOICES = ( 
        ('Backlog','Backlog'),
        ('Waiting On Submitter','Waiting On Submitter'),
        ('In Progress','In Progress'),
        ('Waiting On Support','Waiting On Support'),
    )

    ticketType = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    subject = models.CharField(max_length=75)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, default='')
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICES, blank=True) #Priority, on_delete=models.CASCADE, blank=True) #needs to be removed and replaced with list
    status = models.CharField(max_length=40,choices=STATUS_CHOICES, blank=True)
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.ticketType.ticketType + '-' + str(self.id)

    def how_many_days_old(self):
        return int(dateformat.format(timezone.now(), 'd')) - int(dateformat.format(self.created_at,'d'))

    def get_comments(self):
        queryset = Comment.objects.filter(ticketID=self.id)
        if queryset:
            return queryset
        else:
            return None

class Attachment(TimeStampMixin): #1 to many
    ticketID = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    filepath = models.CharField(max_length=150)

class Comment(TimeStampMixin): #1 to many
    ticketID = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

