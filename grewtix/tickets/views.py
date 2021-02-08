from django.shortcuts import get_object_or_404, render
from django.views import generic 
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin, TemplateResponseMixin
from django.http import HttpResponse, HttpResponseRedirect
from os import path

from .forms import TicketForm, CommentForm
from .models import Ticket, Comment

def TicketAssign(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.owner = User.objects.get(id=request.user.id)
    ticket.save()
    return HttpResponseRedirect(reverse('tickets:edit', kwargs={'pk': ticket.id}))

def CommentOnTicket(request, comment):
    pass

def index(request):
    return render(request, 'tickets/index.html')

def ticketedit(request):
    split_path = path.split(request.path)
    ticket_split_by_dash = split_path[1].split('-')
    ticket_id = ticket_split_by_dash[1]
    if Ticket.objects.filter(pk=int(ticket_id)).exists():
        ticket_object = Ticket.objects.get(pk=int(ticket_id))
        if split_path[1].lower() == str(ticket_object).lower():
            return HttpResponseRedirect(reverse('tickets:edit', kwargs={'pk': ticket_id}))
    else:
        return HttpResponse("Could not find the ticket you are looking for.") 

def reports(request):
    return render(request, 'tickets/ticket_reports.html')


##############################
# Returns different query sets for the ticket class
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
##############################

##############################
# Handles all the CRUD operations for ticket
class TicketFormView():
    model = Ticket
    form_class = TicketForm

    def get_success_url(self):
        return reverse('tickets:index')

class TicketCreate(TicketFormView, CreateView):
    template_name = 'tickets/ticket_create_form.html'
    form_class = TicketForm


class TicketUpdate(TicketFormView, UpdateView):
    template_name = 'tickets/ticket_update_form.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # context['ticket_form'] = TicketForm
        context['comment_form'] = CommentForm
        return context

class TicketDelete(TicketFormView, DeleteView):
    pass

# class MultiFormViews(TemplateResponseMixin, BaseMul)

##############################