from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import validate_email

from website.models import Users, SystemAdmin, Author, ConferenceChair, Reviewer

def createNewUser(request):

    if(request.POST):
        selectedRole = request.POST['roleList']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if(CheckEmailinDB(email) == False):
            messages.error(request, "Invalid Email. This email exists in the DB already.")
            return redirect('register')

        if(validateEmail(email) == False):
            messages.error(request, "Invalid Email. Please ensure the email is in the valid format.")
            return redirect('register')

        if(CheckUsernameinDB(username) == False):
            messages.error(request, "Invalid username. This username exists in the DB already.")
            return redirect('register')

        #Add user base on their roles
        if(selectedRole == "Author"):
            name = request.POST['fullname']

            success = Author.createAuthor(email, username, password, name)

            if(success):
                messages.success(request, "Successfully created Author.")
            else:
                messages.error(request, "Invalid input found. Please ensure all fields are filled.")

        elif (selectedRole == "Reviewer"):
            name = request.POST['fullname']
            maxpaper = request.POST['maxpaper']

            success = Reviewer.createReviewer(email, username, password, name, maxpaper)

            if(success):
                messages.success(request, "Successfully created Reviewer.")
            else:
                messages.error(request, "Invalid input found. Please ensure all fields are filled.")

        elif(selectedRole == "Conference Chair"):
            name = request.POST['fullname']

            success = ConferenceChair.CreateConferenceChair(email, username, password, name)

            if(success):
                messages.success(request, "Successfully created Conference Chair.")
            else:
                messages.error(request, "Invalid input found. Please ensure all fields are filled.")

        elif(selectedRole == "System Admin"):

            success = SystemAdmin.createSystemAdmin(email, username, password)

            if(success):
                messages.success(request, "Successfully created System Admin.")
            else:
                messages.error(request, "Invalid input found. Please ensure all fields are filled.")

        return redirect('register')

    return render(request, 'admin/create_user.html', {})


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
