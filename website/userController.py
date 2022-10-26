from django.template import loader
from django.urls import reverse

from django.shortcuts import render, redirect

from .models import Users

def db(request):
    myusers = Users.objects.all().values()
    context = {'myusers':myusers}

    return render(request, 'db.html', context)

def register(request):

    return render(request, 'register.html', {})

def addNewUser(request):
    new_fullname = request.POST['fullname']
    new_username = request.POST['username']
    new_password = request.POST['password']

    user = Users.createUser(new_fullname, new_username, new_password)
    user.save()

    return redirect('db')

def update(request,id):
    myuser = Users.objects.get(id=id)
    context = {'myuser':myuser}

    return render(request, 'update.html', context)

def updateProfile(request, id):
    new_fullname = request.POST['fullname']
    new_username = request.POST['username']
    new_password = request.POST['password']
    
    user = Users.objects.get(id=id)
    user.updateUser(new_fullname, new_username, new_password)
    user.save()

    return redirect('db')

    
     