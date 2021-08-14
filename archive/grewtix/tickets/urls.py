from django.urls import path, re_path

from . import views

app_name = 'tickets'
urlpatterns = [
    path('', views.index, name='index'),
    path('owned_by_user_queue/', views.OwnedByUserView.as_view(), name='owned_by_user_queue'),
    path('created_by_user_queue/', views.CreatedByUserView.as_view(), name='created_by_user_queue'),
    path('unassigned_queue/', views.UnassignedView.as_view(), name='unassigned_queue'),
    path('recently_created_queue/', views.RecentlyCreatedView.as_view(), name='recently_created_queue'),
    path('all_ticket_queue/', views.AllTicketsView.as_view(), name='all_ticket_queue'),

    path('create/', views.TicketCreate.as_view(), name='create'),
    # re_path(r'^edit/[a-zA-Z]+[-][0-9]+', views.ticketedit, name='edit'),
    path('edit/<int:pk>', views.TicketUpdate.as_view(), name='edit'),
    path('<pk>/delete/', views.TicketDelete.as_view(), name='delete'),
    path('assign/<int:ticket_id>', views.TicketAssign, name="assign"),
    path('reports/', views.reports, name="reports")
    #path('comment/<int:comment>', views.CommentOnTicket, name="comment"),
]