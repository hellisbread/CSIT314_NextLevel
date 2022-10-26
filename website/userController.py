from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Users

def db(request):
    myusers = Users.objects.all().values()
    template = loader.get_template('db.html')
    context = {'myusers':myusers}

    return HttpResponse(template.render(context,request))

def register(request):
    template = loader.get_template('register.html')
    
    return HttpResponse(template.render({}, request))

def addNewUser(request):
    new_fullname = request.POST['fullname']
    new_username = request.POST['username']
    new_password = request.POST['password']

    user = Users.createUser(new_fullname, new_username, new_password)
    user.save()

    return HttpResponseRedirect(reverse('db'))

def update(request,id):
    myuser = Users.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {'myuser':myuser}

    return HttpResponse(template.render(context, request))

def updateProfile(request, id):
    new_fullname = request.POST['fullname']
    new_username = request.POST['username']
    new_password = request.POST['password']
    user = Users.objects.get(id=id)
    user.updateUser(new_fullname, new_username, new_password)
    user.save()

    return HttpResponseRedirect(reverse('db'))

    
     