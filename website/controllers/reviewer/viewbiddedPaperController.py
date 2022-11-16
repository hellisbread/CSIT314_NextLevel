from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

from website.models import Users, Reviewer, Paper, Bidded_Paper, Review, Comment

def biddedPaperPage(request):

    reviewer_id = request.session['ReviewerLogged']

    context = Bidded_Paper.getAllAssignedAndReviewedPapers(reviewer_id)

    return render(request, 'reviewer/view_bidded_papers.html', context)
