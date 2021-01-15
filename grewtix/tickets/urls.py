from django.urls import path

from . import views

app_name = 'tickets'
urlpatterns = [
    path('', views.RecentlyCreatedView.as_view(), name='index'),
    path('create/', views.TicketCreate.as_view(), name='create'),
    path('edit/<int:pk>', views.TicketUpdate.as_view(), name='edit'),
    path('<pk>/delete/', views.TicketDelete.as_view(), name='delete'),
    path('assign/<int:ticket>', views.TicketAssign, name="assign"),
    # path('<int:ticket_id>/', views.ticket_edit_view, name='edit')
]