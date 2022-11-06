from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Users, Reviewer

def reviewerPage(request):
    return render(request, 'reviewer.html', {})

def bidPaper(request):
    return render(request, 'bid_paper.html', {})

def settings(request):
    return render(request, 'settings.html', {})

def biddedPaperPage(request):
    return render(request, 'view_bidded_papers.html', {})

def toReviewPaperPage(request):
    return render(request, 'view_papers_to_review.html', {})