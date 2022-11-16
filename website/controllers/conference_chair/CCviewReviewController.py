
from django.shortcuts import render
from ...models import Review, Paper
from django.db.models import Q

from django.contrib import messages

def viewReview(request, id):
    reviews = Review.getAllReviewByPaperID(id)
    numberOfReview = reviews.count()

    if reviews.count() > 0:
        paper = Paper.getPaper(id)
        text = Paper.readSubmittedPaper(id)
        context = {'reviews' : reviews, 'numberOfReview' : numberOfReview, 'paper': paper, 'content':text}

        return render(request, 'conferenceChair/viewReview.html', context)