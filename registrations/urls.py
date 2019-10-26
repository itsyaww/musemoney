from django.urls import path

from . import views

app_name = 'registrations'

urlpatterns = [
    path('', views.logon, name='logon'),
    path('create', views.adduser, name='adduser'),
    path('verify', views.logon, name='logon'),
    path('signup', views.signup, name='signup')
]