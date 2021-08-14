from django.shortcuts import render
from django.views import generic
from tickets.models import Ticket

# Create your views here.


def ticket_index(request):
    return render(request, 'ticket_index.html')


def reports(request):
    return render(request, 'ticket_reports.html')


class TicketListView(generic.ListView):
    template_name = "ticket_display_queryset.html"
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
