from django.template import loader
from django.contrib import messages

from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import validate_email

from .models import Users, Author, ConferenceChair, Reviewer, SystemAdmin

def register(request):

    if(request.POST):
        selectedRole = request.POST['roleList']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if(validateEmail(email) == False):
            messages.error(request, "Invalid Email Found. Please ensure this email has not been used and is valid.")
            return redirect('register')

        if(validateUsername(username) == False):
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

def updateAuthors(request, id):

    if(request.POST):

        name = request.POST['fullname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        success = Author.UpdateAuthorByID(id,email,username,password,name)

        if(success):
            messages.success(request, "Successfully updated Author ID: " + str(id))
            return redirect('systemAdminPage')
        else:
            messages.error(request, "There was an error updating.")
            return redirect('systemAdminPage')

    else:
        myauthor = Author.getAuthorByID(id)
        context = {'author':myauthor}

        return render(request, 'admin/update_author.html', context)

def updateReviewers(request,id):
    if(request.POST):

        name = request.POST['fullname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        maxPaper = request.POST['maxPaper']

        success = Reviewer.UpdateReviewerByID(id,email,username,password,name,maxPaper)

        if(success):
            messages.success(request, "Successfully updated Reviewer ID: " + str(id))
            return redirect('systemAdminPage')
        else:
            messages.error(request, "There was an error updating.")
            return redirect('systemAdminPage')

    else:
        myreviewer = Reviewer.getReviewerByID(id)
        context = {'reviewer':myreviewer}

        return render(request, 'admin/update_reviewer.html', context)

def updateConfs(request,id):
    if(request.POST):

        name = request.POST['fullname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        success = ConferenceChair.UpdateConferenceChairByID(id,email,username,password,name)

        if(success):
            messages.success(request, "Successfully updated Conference Chair ID: " + str(id))
            return redirect('systemAdminPage')
        else:
            messages.error(request, "There was an error updating.")
            return redirect('systemAdminPage')

    else:
        myconf = ConferenceChair.getConferenceChairByID(id)
        context = {'conference':myconf}

        return render(request, 'admin/update_conference.html', context)

def updateAdmins(request,id):
    if(request.POST):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        success = SystemAdmin.UpdateSysAdminByID(id,email,username,password)

        if(success):
            messages.success(request, "Successfully updated System Admin ID: " + str(id))
            return redirect('systemAdminPage')
        else:
            messages.error(request, "There was an error updating.")
            return redirect('systemAdminPage')

    else:
        myadmin = SystemAdmin.getSystemAdminByID(id)
        context = {'admin':myadmin}

        return render(request, 'admin/update_admin.html', context)

    

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


     