from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

from .models import Users, Reviewer, Paper, Bidded_Paper

def reviewerPage(request):
    return render(request, 'reviewer/reviewer.html', {})

def bidPaper(request):

    reviewer_id = request.session['ReviewerLogged']

    paper_list = Paper.getAllUnbiddedPaper(reviewer_id)


    context = {'papers':paper_list}

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
    return render(request, 'reviewer/settings.html', {})

def biddedPaperPage(request):

    reviewer_id = request.session['ReviewerLogged']

    bid_list = Bidded_Paper.getAllBiddedPaperByID(reviewer_id)

    context = {'bid_list':bid_list}

    print(context)

    return render(request, 'reviewer/view_bidded_papers.html', context)

def reviewPage(request, id):
    return render(request, 'reviewer/review_paper.html', {})