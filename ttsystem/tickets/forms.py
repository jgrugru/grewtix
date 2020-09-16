from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        # fields = "__all__"
        
        widgets = {
        #     'subject' : forms.TextInput(attrs={"class": "form-control-plaintext bg-light"})
            'description': forms.Textarea()
        }

        fields = [
            'ticketType',
            'subject',
            'project',
            'description',
            'priority',
            'status',
        #     'creation_date',
        #     'creator',
            'owner',
        ]