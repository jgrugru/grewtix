from django.urls import path

from . import views

app_name = 'tickets'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.TicketCreate.as_view(), name='create'),
    path('edit/<int:pk>', views.TicketUpdate.as_view(), name='edit'),
    # path('<int:ticket_id>/', views.ticket_edit_view, name='edit')
]