from django.db import models
from django.utils import timezone

# Create your models here.

class TicketType(models.Model): #1 to many
    ticketType = models.CharField(max_length=5)
    
    def __str__(self):
        return self.ticketType

class Project(models.Model): #1 to many
    project = models.CharField(max_length=45)

    def __str__(self):
        return self.project

class Priority(models.Model): #1 to many
    priority = models.CharField(max_length=10)

    def __str__(self):
        return self.priority

class Status(models.Model): #1 to many
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status

class Ticket(models.Model):
    ticketType = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    subject = models.CharField(max_length=75)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default='')
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date')

    def __str__(self):
        return self.subject

class Attachment(models.Model): #1 to many
    ticketID = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    filepath = models.CharField(max_length=150)
    creationDate = models.DateTimeField('creation date')

class Comment(models.Model): #1 to many
    ticketID = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    creationDate = models.DateTimeField('creation date')
