from django.shortcuts import get_object_or_404, render, Http404
from django.http import HttpResponse
from django.template import loader
from django.views import generic 
from django.urls import reverse

from .models import Ticket

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'tickets/index.html'
    context_object_name = 'latest_ticket_list'

    def get_queryset(self):
        """Return the last five published Tickets."""
        return Ticket.objects.order_by('-creation_date')[:5]

def detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'tickets/detail.html', {'ticket': ticket})