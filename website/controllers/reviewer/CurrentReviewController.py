from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone

from website.models import Reviewer, Bidded_Paper, Review

def currentReviews(request, id):
    reviewer_id = request.session['ReviewerLogged']

    bidPaper = Bidded_Paper.getBiddedPaper(id)

    other_reviews = Review.getOtherReviews(bidPaper.paper_id, reviewer_id)

    #Get Reviewer Name base on reviewer ID
    for otherReview in other_reviews:
        print(otherReview)
        reviewer_name = Reviewer.getReviewerByID(otherReview.get("reviewer_id")).name
        otherReview['reviewerName'] = reviewer_name

    context = {'bid_id':id, 'other_reviews':other_reviews}

    print(context)

    return render(request, 'reviewer/current_reviews.html', context)