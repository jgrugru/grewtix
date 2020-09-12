from django.urls import path

from . import views

app_name = 'tickets'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:ticket_id>/', views.detail, name='detail')
]