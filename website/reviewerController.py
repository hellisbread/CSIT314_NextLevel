from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

from .models import Users, Reviewer, Paper, Bidded_Paper

def reviewerPage(request):
    return render(request, 'reviewer/reviewer.html', {})

def bidPaper(request):

    paper_list = Paper.getAllPaper()

    context = {'papers':paper_list}

    return render(request, 'reviewer/bid_paper.html', context)

def addBidPaper(request, id):

    reviewer_id = request.session['ReviewerLogged']

    paper = Paper.getPaper(id)

    success = Bidded_Paper.createBiddedPaper(reviewer_id, paper, "0")

    if(success):
        messages.success(request, "Successfully bidded for paper - "+paper.topic)
        return redirect('reviewerPage')

    return render(request, 'reviewer/bid_paper.html', {})


def settings(request):
    return render(request, 'reviewer/settings.html', {})

def biddedPaperPage(request):
    return render(request, 'reviewer/view_bidded_papers.html', {})

def reviewPage(request, id):
    return render(request, 'reviewer/review_paper.html', {})