from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Users, Reviewer, Paper, Bidded_Paper

def reviewerPage(request):
    return render(request, 'reviewer/reviewer.html', {})

def bidPaper(request):

    paper_list = Paper.getAllPaper()

    context ={'papers':paper_list}

    return render(request, 'reviewer/bid_paper.html', context)

def addBidPaper(request, id):

    return render(request, 'reviewer/bid_paper.html', {})


def settings(request):
    return render(request, 'reviewer/settings.html', {})

def biddedPaperPage(request):
    return render(request, 'reviewer/view_bidded_papers.html', {})

def reviewPage(request, id):
    return render(request, 'reviewer/review_paper.html', {})