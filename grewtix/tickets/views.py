from django.shortcuts import get_object_or_404, render
from django.views import generic 
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse

from .forms import TicketForm
from .models import Ticket, Comment

def TicketAssign(request, ticket):
    ticket = Ticket.objects.get(id=ticket)
    ticket.owner = User.objects.get(id=request.user.id)
    ticket.save()
    return CreatedByUserView.as_view()(request)

def index(request):
    return render(request, 'tickets/index.html')

def ticketedit(request):
    return render(request, 'tickets/index.html')
 
# Create your views here.
class TicketListView(generic.ListView):
    template_name = 'tickets/ticket_display_queryset.html'
    context_object_name = 'ticket_list'

class RecentlyCreatedView(TicketListView):
    def get_queryset(self):
        """Return the last five published Tickets."""
        return Ticket.objects.order_by('-created_at')[:4]

class OwnedByUserView(TicketListView):
    def get_queryset(self):
        return Ticket.objects.filter(owner=self.request.user.id).order_by('-created_at')

class CreatedByUserView(TicketListView):
    def get_queryset(self):
        return Ticket.objects.filter(creator=self.request.user.id).order_by('-created_at')

class UnassignedView(TicketListView):
    def get_queryset(self):
        return Ticket.objects.filter(owner=None).order_by('-created_at')

class AllTicketsView(TicketListView):
    def get_queryset(self):
        return Ticket.objects.all().order_by('-created_at')

class FormViews():
    model = Ticket
    form_class = TicketForm

    def get_success_url(self):
        return reverse('tickets:index')

class TicketCreate(FormViews, CreateView):
    template_name = 'tickets/ticket_create_form.html'

class TicketUpdate(FormViews, UpdateView):

    template_name_suffix = '_update_form'

class TicketDelete(FormViews, DeleteView):
    pass
