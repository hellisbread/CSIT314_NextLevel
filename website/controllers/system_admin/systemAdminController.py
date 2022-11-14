from django.shortcuts import render,redirect
from django.contrib import messages

from website.models import Users, Author, ConferenceChair, Reviewer, SystemAdmin

def systemAdminPage(request):

    if 'SysAdminLogged' in request.session:
        Authors = Author.getAllActiveAuthor()
        ConfChairs = ConferenceChair.getAllActiveConferenceChair()
        Reviewers = Reviewer.getAllActiveReviewer()
        SysAdmins = SystemAdmin.getAllActiveSystemAdmin()

        context = {'authors':Authors,'confchairs':ConfChairs,'reviewers':Reviewers,'sysadmins':SysAdmins}

        print(context)

        return render(request, 'admin/systemAdmin.html', context)
    else:
        messages.error(request, "Please login before accessing this page.")
        return redirect('index')

