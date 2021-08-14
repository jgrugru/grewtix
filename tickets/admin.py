from django.contrib import admin
from tickets.models import Ticket, TicketType, Project


# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    pass


class TicketTypeAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ticket, TicketAdmin)
admin.site.register(TicketType, TicketTypeAdmin)
admin.site.register(Project, ProjectAdmin)
