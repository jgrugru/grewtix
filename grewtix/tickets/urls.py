from django.urls import path

from . import views

app_name = 'tickets'
urlpatterns = [
    path('', views.index, name='index'),
    path('my_queue/', views.OwnedByUserView.as_view(), name='my_queue'),
    path('tickets_created/', views.CreatedByUserView.as_view(), name='created_by_user_queue'),
    path('unassigned_queue/', views.UnassignedView.as_view(), name='unassigned_queue'),
    path('recently_created_queue/', views.RecentlyCreatedView.as_view(), name='recently_created_queue'),
    path('all_ticket_queue/', views.AllTicketsView.as_view(), name='all_ticket_queue'), #this is not returning all the tickets... Will look into it.
    path('create/', views.TicketCreate.as_view(), name='create'),
    path('edit/<int:pk>', views.TicketUpdate.as_view(), name='edit'),
    path('<pk>/delete/', views.TicketDelete.as_view(), name='delete'),
    path('assign/<int:ticket>', views.TicketAssign, name="assign"),
    # path('<int:ticket_id>/', views.ticket_edit_view, name='edit')
]