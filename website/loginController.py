from django.template import loader
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users

# log in page
def index(request):

    return render(request, 'index.html', {})

def checkLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    myusers = Users.objects.values_list()

    for x in myusers:
        if x[2] == username and x[3] == password:
            return redirect(request, 'success.html', {})
        
    messages.error(request, 'username or password is not correct')
    return redirect('index')