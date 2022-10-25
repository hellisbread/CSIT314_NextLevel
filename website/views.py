from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    
    return HttpResponse(template.render({}, request))

def db(request):
    myusers = Users.objects.all().values()
    template = loader.get_template('db.html')
    context = {'myusers':myusers}

    return HttpResponse(template.render(context,request))

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render({}, request))

def adduser(request):
    new_fullname = request.POST['fullname']
    new_username = request.POST['username']
    new_password = request.POST['password']
    user = Users(Name = new_fullname, username = new_username, password = new_password)
    user.addNewUser()

    return HttpResponseRedirect(reverse('db'))

def delete(request, id):
    user = Users.objects.get(id=id)
    user.delete()

    return HttpResponseRedirect(reverse('db'))

def update(request,id):
    myuser = Users.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {'myuser':myuser}

    return HttpResponse(template.render(context, request))

def updateprofile(request, id):
    new_fullname = request.POST['fullname']
    new_username = request.POST['username']
    new_password = request.POST['password']
    user = Users.objects.get(id=id)
    user.fullname = new_fullname
    user.lastname = new_username
    user.password = new_password
    user.save()

    return HttpResponseRedirect(reverse('db'))