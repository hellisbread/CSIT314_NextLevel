from django.shortcuts import render

from website.models import Users, Author, ConferenceChair, Reviewer, SystemAdmin

def systemAdminPage(request):

    Authors = Author.getAllActiveAuthor()
    ConfChairs = ConferenceChair.getAllActiveConferenceChair()
    Reviewers = Reviewer.getAllActiveReviewer()
    SysAdmins = SystemAdmin.getAllActiveSystemAdmin()

    context = {'authors':Authors,'confchairs':ConfChairs,'reviewers':Reviewers,'sysadmins':SysAdmins}

    print(context)

    return render(request, 'admin/systemAdmin.html', context)

