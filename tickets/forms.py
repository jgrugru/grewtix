from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket

        widgets = {
            'description': forms.Textarea(),
            'creator': forms.HiddenInput(),
            }

        fields = [
            'ticketType',
            'subject',
            'project',
            'description',
            'priority',
            'status',
            'creator',
            'owner',
        ]
