from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=14)

class TicketType(models.Model): #1 to many
    subject = models.CharField(max_length=5)

class Project(models.Model): #1 to many
    project = models.CharField(max_length=45)

class Priority(models.Model): #1 to many
    priority = models.CharField(max_length=10)

class Status(models.Model): #1 to many
    status = models.CharField(max_length=20)

class Attachment(models.Model): #1 to many
    filepath = models.CharField(max_length=150)
    creationDate = models.DateTimeField('creation date')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model): #1 to many
    comment = models.CharField(max_length=500)
    creationDate = models.DateTimeField('creation date')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class Ticket(models.Model):
    ticketType = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    subject = models.CharField(max_length=75)
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    description = models.CharField(max_lenght=1000, default='')
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticketType + '-' + self.subject
