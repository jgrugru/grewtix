from django.shortcuts import get_object_or_404, render, Http404
from django.http import HttpResponse
from django.template import loader
from django.views import generic 
from django.urls import reverse

from .forms import TicketForm
from .models import Ticket

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'tickets/index.html'
    context_object_name = 'latest_ticket_list'

    def get_queryset(self):
        """Return the last five published Tickets."""
        return Ticket.objects.order_by('-created_at')[:5]

def detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'tickets/detail.html', {'ticket': ticket})

def ticket_create_view(request):
    form = TicketForm(request.POST or None)
    print(form)
    if form.is_valid():
        form.save()
        form = TicketForm()

    return render(request, 'tickets/ticket_create.html', {'form': form})
