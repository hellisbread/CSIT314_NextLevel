from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

from website.models import Users, Reviewer, Paper, Bidded_Paper, Review, Comment

def biddedPaperPage(request):

    reviewer_id = request.session['ReviewerLogged']

    assigned_list = Bidded_Paper.getAllAssignedPaperByID(reviewer_id)

    completed_list = Bidded_Paper.getAllReviewedPaperByID(reviewer_id)

    context = {'assigned_list':assigned_list,'completed_list':completed_list}

    print(context)

    return render(request, 'reviewer/view_bidded_papers.html', context)
