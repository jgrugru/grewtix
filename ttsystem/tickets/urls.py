from django.urls import path

from . import views

app_name = 'tickets'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.ticket_create_view, name='create'),
    path('<int:ticket_id>/', views.ticket_edit_view, name='edit')
]