from django.contrib import admin

from .models import TicketType, Project, Priority, Status, Ticket, Attachment, Comment
# Register your models here.
admin.site.register(TicketType)
admin.site.register(Project)
admin.site.register(Priority)
admin.site.register(Status)
admin.site.register(Ticket)
admin.site.register(Attachment)
admin.site.register(Comment)