from django.template import loader
from django.contrib import messages

from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import validate_email

from .models import Users, Author, ConferenceChair, Reviewer, SystemAdmin

def db(request):

    Authors = Author.getAllAuthor()
    ConfChairs = ConferenceChair.getAllConferenceChair()
    Reviewers = Reviewer.getAllReviewer()
    SysAdmins = SystemAdmin.getAllSystemAdmin()

    context = {'authors':Authors,'confchairs':ConfChairs,'reviewers':Reviewers,'sysadmins':SysAdmins}

    return render(request, 'db.html', context)

def register(request):

    return render(request, 'register.html', {})

def addNewUser(request):
    if(request.POST):
        selectedRole = request.POST['roleList']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if(validateEmail(email) == False):
            messages.error(request, "Invalid Email Found. Please ensure this email has not been used and is valid.")
            register(request)

        if(validateUsername(username) == False):
            messages.error(request, "Invalid username. This username exists in the DB already.")
            register(request)

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

def validateEmail(email) -> bool:

    #Check if email exists in db
    try:
        if(Users.objects.filter(email = email).exists()):
            return False
    except ObjectDoesNotExist:
        #Check if email is in the correct format
        try:
            validate_email(email)
            return True
        except ValidationError as e:
            return False

def validateUsername(username) -> bool:
    #Check if username exists in DB
    if(Users.objects.filter(username = username).exists()):
        return False
    else:
        return True

def update(request,id):
    myuser = Users.objects.get(id=id)
    context = {'myuser':myuser}

    return render(request, 'update.html', context)

def updateProfile(request, id):

    #Only if a POST has been initiated
    if(request.POST):
        new_fullname = request.POST['fullname']
        new_username = request.POST['username']
        new_password = request.POST['password']
        
        user = Users.objects.get(id=id)
        user.updateUser(new_fullname, new_username, new_password)
        user.save()

        return redirect('db')

    else:
        return redirect('index')

    
     