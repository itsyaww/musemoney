from django.urls import path

from . import views

app_name = 'registrations'

urlpatterns = [
    path('', views.index, name='index'),
]