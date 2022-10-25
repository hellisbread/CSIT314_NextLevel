from django.http import HttpResponse
from django.template import loader
from .models import Users

def checkLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    myusers = Users.objects.values_list()

    templateSuccess = loader.get_template('success.html')
    templateFail = loader.get_template('fail.html')
    for x in myusers:
        if x[2] == username and x[3] == password:
            return HttpResponse(templateSuccess.render({},request))
        else:
            return HttpResponse(templateFail.render({},request))    