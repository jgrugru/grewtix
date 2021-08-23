from django.urls import path
from . import views

app_name = 'tickets'
urlpatterns = [
    path("", views.ticket_index, name="ticket_index"),
    path('create/', views.TicketCreate.as_view(), name='ticket_create'),
    path('detail/<int:pk>', views.TicketDetail.as_view(), name='ticket_detail'),
    path('edit/<int:pk>', views.TicketUpdate.as_view(), name='ticket_edit'),
    path('delete/<int:pk>', views.TicketDelete.as_view(), name='ticket_delete'),

    path('owner/', views.OwnedByUserView.as_view(), name='ticket_owner_queue'),
    path('created_by/', views.CreatedByUserView.as_view(), name='ticket_created_queue'),
    path('unassigned/', views.UnassignedView.as_view(), name='ticket_unassigned_queue'),
    path('recent/', views.RecentlyCreatedView.as_view(), name='ticket_recent_queue'),
    path('all/', views.AllTicketsView.as_view(), name='ticket_all_queue'),

    path('reports/', views.reports, name="ticket_reports"),
]
