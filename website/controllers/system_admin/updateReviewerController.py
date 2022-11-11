from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import validate_email

from website.models import Users, Reviewer

def updateReviewers(request,id):
    if(request.POST):

        role = request.POST['roleList']
        name = request.POST['fullname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        maxPaper = request.POST['maxPaper']

        myreviewer = Reviewer.getReviewerByID(id)

        if(CheckEmailinDB(email) == False and email!=myreviewer.email):
            messages.error(request, "Invalid Email. This email exists in the DB already.")
            return redirect('update_reviewer', id=id)

        if(validateEmail(email) == False and email!=myreviewer.email):
            messages.error(request, "Invalid Email. Please ensure the email is in the valid format.")
            return redirect('update_reviewer', id=id)

        if(CheckUsernameinDB(username) == False and username!=myreviewer.username):
            messages.error(request, "Invalid username. This username exists in the DB already.")
            return redirect('update_reviewer', id=id)

        #Updating
        if(role=="Reviewer"):
            success = Reviewer.UpdateReviewerByID(id,email,username,password,name, maxPaper)
        else:
            success = Reviewer.UpdateRoleByID(id,email,username,password,name,maxPaper,role)

        if(success):
            messages.success(request, "Successfully updated Reviewer ID: " + str(id))
            return redirect('systemAdminPage')
        else:
            messages.error(request, "There was an error updating.")
            return redirect('update_reviewer', id=id)

    else:
        myreviewer = Reviewer.getReviewerByID(id)
        context = {'reviewer':myreviewer}

        return render(request, 'admin/update_reviewer.html', context)

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