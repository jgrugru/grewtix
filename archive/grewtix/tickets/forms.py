from django import forms
from .models import Ticket, Comment

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        
        widgets = {
        #     'subject' : forms.TextInput(attrs={"class": "form-control-plaintext bg-light"})
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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        widgets = {
            'comment': forms.Textarea(),
            'creator': forms.HiddenInput(),
        }

        fields = ['comment', 'creator']