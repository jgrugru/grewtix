from django.shortcuts import get_object_or_404, render, Http404
from django.http import HttpResponse
from django.template import loader

from .models import Ticket

# Create your views here.
def index(request):
    latest_ticket_list = Ticket.objects.all()
    context = {'latest_ticket_list': latest_ticket_list}
    # output = ', '.join([t.ticketType.ticketType + '-' + str(t.id) for t in latest_ticket_list])
    return render(request, 'tickets/index.html', context)

def detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'tickets/detail.html', {'ticket': ticket})