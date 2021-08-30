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

        # help_texts = {
        #     'subject': 'Group to which this message belongs to',
        # }

        # error_messages={
        #     'required': 'Please enter your name'
        # }
