from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"
        
        # widgets = {
        #     'class' : 'form-control'
        # }

        # fields = [
        #     'ticketType',
        #     'subject',
        #     'project',
        #     'description',
        #     'priority',
        #     'owner',
        #     'status',
        #     'creation_date',
        #     'creator',
        #     'owner',
        # ]