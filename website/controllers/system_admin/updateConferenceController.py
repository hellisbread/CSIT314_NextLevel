from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import validate_email

from website.models import Users, ConferenceChair

def updateConfs(request,id):
    if(request.POST):

        role = request.POST['roleList']
        name = request.POST['fullname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        myconf = ConferenceChair.getConferenceChairByID(id)

        if(CheckEmailinDB(email) == False and email!=myconf.email):
            messages.error(request, "Invalid Email. This email exists in the DB already.")
            return redirect('update_conference', id=id)

        if(validateEmail(email) == False and email!=myconf.email):
            messages.error(request, "Invalid Email. Please ensure the email is in the valid format.")
            return redirect('update_conference', id=id)

        if(CheckUsernameinDB(username) == False and username!=myconf.username):
            messages.error(request, "Invalid username. This username exists in the DB already.")
            return redirect('update_conference', id=id)

        #Updating
        if(role=="Conference Chair"):
            success = ConferenceChair.UpdateConferenceChairByID(id,email,username,password,name)
        else:
            maxPaper = request.POST['maxPaper']
            success = ConferenceChair.UpdateRoleByID(id,email,username,password,name,maxPaper,role)

        if(success):
            messages.success(request, "Successfully updated Conference Chair ID: " + str(id))
            return redirect('systemAdminPage')
        else:
            messages.error(request, "There was an error updating.")
            return redirect('update_conference', id=id)

    else:
        myconf = ConferenceChair.getConferenceChairByID(id)
        context = {'conference':myconf}

        return render(request, 'admin/update_conference.html', context)


def CheckEmailinDB(email) -> bool:

    #Check if email exists in db
    try:
        if(Users.objects.filter(email = email).exists()):
            return False
    except ObjectDoesNotExist:
        #Check if email is in the correct format
        try:
            validate_email(email)
            print('good email!')
            return True
        except ValidationError as e:
            print('error found!')
            return False

def validateEmail(email) -> bool:

    try:
        validate_email(email)
        print('good email!')
        return True
    except ValidationError as e:
        print('error found!')
        return False

def CheckUsernameinDB(username) -> bool:
    #Check if username exists in DB
    if(Users.objects.filter(username = username).exists()):
        return False
    else:
        return True