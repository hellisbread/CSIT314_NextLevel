from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib import messages
from .models import Users

# log in page
def index(request):
    template = loader.get_template('index.html')
    
    return HttpResponse(template.render({}, request))

def checkLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    myusers = Users.objects.values_list()

    templateSuccess = loader.get_template('success.html')
    for x in myusers:
        if x[2] == username and x[3] == password:
            return HttpResponse(templateSuccess.render({},request))
        
    messages.error(request, 'username or password is not correct')
    return redirect('index')