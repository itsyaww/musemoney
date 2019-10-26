from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def logon(request):
    return render(request, 'registrations/logon.html')

def adduser(request):
    fname = request.POST.get('firstname')
    lname = request.POST.get('lastname')
    email = request.POST.get('email')
    pword = request.POST.get('password')
    user = User.objects.create_user(fname, email, pword)
    user.lastname = lname
    user.save()
    return HttpResponseRedirect(reverse('registrations:logon'))

def signup(request):
    return render(request, 'registrations/signup.html')

def verify(request):
    uname = request.POST['username']
    pword = request.POST['password']
    user = authenticate(username=uname, password=pword)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('registrations:home'))
    else:
        return render(request, 'registrations/logon.html', {
            'error_message': "Your details were incorrect, please try again",
        })