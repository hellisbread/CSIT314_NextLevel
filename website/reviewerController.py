from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

from .models import Users, Reviewer, Paper, Bidded_Paper

def reviewerPage(request):
    return render(request, 'reviewer/reviewer.html', {})

def bidPaper(request):

    reviewer_id = request.session['ReviewerLogged']

    maxPaper = Reviewer.getMaxPaperByID(reviewer_id)

    paper_list = Paper.getAllUnbiddedPaper(reviewer_id)

    context = {'papers':paper_list, 'max_paper': maxPaper}

    print(context)

    return render(request, 'reviewer/bid_paper.html', context)

def addBidPaper(request, id):

    reviewer_id = request.session['ReviewerLogged']

    paper = Paper.getPaper(id)

    if(paper==None):
        messages.error(request, "Unable to find paper - Please try again.")
        return redirect('reviewerPage')

    success = Bidded_Paper.createBiddedPaper(reviewer_id, paper, "0")

    if(success):
        messages.success(request, "Successfully bidded for paper - "+paper.topic)
        return redirect('reviewerPage')
    else:
        messages.error(request, "An error has occured while adding paper")

    return render(request, 'reviewer/bid_paper.html', {})


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

def biddedPaperPage(request):

    reviewer_id = request.session['ReviewerLogged']

    unassigned_list = Bidded_Paper.getAllUnassignedPaperByID(reviewer_id)

    assigned_list = Bidded_Paper.getAllAssignedPaperByID(reviewer_id)

    completed_list = Bidded_Paper.getAllReviewedPaperByID(reviewer_id)

    context = {'unassigned_list':unassigned_list,'assigned_list':assigned_list,'completed_list':completed_list}

    print(context)

    return render(request, 'reviewer/view_bidded_papers.html', context)

def reviewPage(request, id):
    return render(request, 'reviewer/review_paper.html', {})