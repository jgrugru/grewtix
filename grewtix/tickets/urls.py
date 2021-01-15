from django.urls import path

from . import views

app_name = 'tickets'
urlpatterns = [
    path('', views.RecentlyCreatedView.as_view(), name='index'),
    path('myqueue/', views.OwnedByUserView.as_view(), name='myqueue'),
    path('tickets_created/', views.CreatedByUserView.as_view(), name='tickets_created'),
    path('unassigned_queue/', views.UnassignedView.as_view(), name='unassigned_queue'),
    path('create/', views.TicketCreate.as_view(), name='create'),
    path('edit/<int:pk>', views.TicketUpdate.as_view(), name='edit'),
    path('<pk>/delete/', views.TicketDelete.as_view(), name='delete'),
    path('assign/<int:ticket>', views.TicketAssign, name="assign"),
    # path('<int:ticket_id>/', views.ticket_edit_view, name='edit')
]