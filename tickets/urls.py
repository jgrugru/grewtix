from django.urls import path
from . import views

app_name = 'tickets'
urlpatterns = [
    path("", views.ticket_index, name="ticket_index"),
    path('owner/', views.OwnedByUserView.as_view(), name='owner_queue'),
    path('created_by/', views.CreatedByUserView.as_view(), name='created_queue'),
    path('unassigned/', views.UnassignedView.as_view(), name='unassigned_queue'),
    path('recent/', views.RecentlyCreatedView.as_view(), name='recent_queue'),
    path('all/', views.AllTicketsView.as_view(), name='all_queue'),

    path('reports/', views.reports, name="ticket_reports"),
]
