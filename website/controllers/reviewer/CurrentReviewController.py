from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone

from website.models import Reviewer, Bidded_Paper, Review

def currentReviews(request, id):
    reviewer_id = request.session['ReviewerLogged']

    other_reviews = Review.getOtherReviews(id, reviewer_id)

    context = {'bid_id':id, 'other_reviews':other_reviews}

    return render(request, 'reviewer/current_reviews.html', context)