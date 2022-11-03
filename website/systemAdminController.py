from django.shortcuts import render, redirect

from .models import Author, ConferenceChair, Reviewer, SystemAdmin

def systemAdminPage(request):

    Authors = Author.getAllAuthor()
    ConfChairs = ConferenceChair.getAllConferenceChair()
    Reviewers = Reviewer.getAllReviewer()
    SysAdmins = SystemAdmin.getAllSystemAdmin()

    context = {'authors':Authors,'confchairs':ConfChairs,'reviewers':Reviewers,'sysadmins':SysAdmins}

    print(context)

    return render(request, 'admin/systemAdmin.html', context)


