from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import validate_email

from website.models import Users, SystemAdmin

def updateAdmins(request,id):
    if(request.POST):
        role = request.POST['roleList']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        myadmin = SystemAdmin.getSystemAdminByID(id)

        if(CheckEmailinDB(email) == False and email!=myadmin.email):
            messages.error(request, "Invalid Email. This email exists in the DB already.")
            return redirect('update_admin', id=id)

        if(validateEmail(email) == False and email!=myadmin.email):
            messages.error(request, "Invalid Email. Please ensure the email is in the valid format.")
            return redirect('update_admin', id=id)

        if(CheckUsernameinDB(username) == False and username!=myadmin.username):
            messages.error(request, "Invalid username. This username exists in the DB already.")
            return redirect('update_admin', id=id)

        #Updating
        if(role=="System Admin"):
            success = SystemAdmin.UpdateSysAdminByID(id,email,username,password)
        else:
            name = request.POST['fullname']
            maxPaper = request.POST['maxPaper']

            success = SystemAdmin.UpdateRoleByID(id,email,username,password,name,maxPaper,role)

        if(success):
            messages.success(request, "Successfully updated System Admin ID: " + str(id))
            return redirect('systemAdminPage')
        else:
            messages.error(request, "There was an error updating.")
            return redirect('update_admin', id=id)

    else:
        myadmin = SystemAdmin.getSystemAdminByID(id)
        context = {'admin':myadmin}

        return render(request, 'admin/update_admin.html', context)



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