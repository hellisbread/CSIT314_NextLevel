from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

from website.models import Reviewer

def settings(request):
    reviewer_id = request.session['ReviewerLogged']

    max_paper = Reviewer.getMaxPaperByID(reviewer_id)

    context = {'max_paper':max_paper}

    return render(request, 'reviewer/settings.html', context)

def updateSettings(request):
    if(request.POST):
        reviewer_id = request.session['ReviewerLogged']

        new_maxPaper = request.POST['maxpaper']

        success = Reviewer.setMaxPaperByID(reviewer_id, new_maxPaper)

        if(success):
            messages.success(request, "Successfully updated max papers.")
        else:
            messages.error(request, "Error updating max paper. Please try again.")

        return redirect('settings')

