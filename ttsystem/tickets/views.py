from django.shortcuts import render
from django.http import HttpResponse

from .models import Ticket

# Create your views here.
def index(request):
    latest_ticket_list = Ticket.objects.all()
    output = ', '.join([t.ticketType.ticketType + '-' + str(t.id) for t in latest_ticket_list])
    return HttpResponse(output)

def detail(request, ticket_id):
    return HttpResponse("You're looking at question %s." % ticket_id)