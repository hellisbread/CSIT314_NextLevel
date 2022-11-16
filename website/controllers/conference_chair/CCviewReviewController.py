
from django.shortcuts import render
from ...models import Review, Paper
from django.db.models import Q

from django.contrib import messages

def viewReview(request, id):
    
    reviews = Review.getAllReviewByPaperID(id)

    paper = Paper.getPaper(id)
    text = Paper.readSubmittedPaper(id)
    context = {'reviews' : reviews, 'paper': paper, 'content':text}

    return render(request, 'conferenceChair/viewReview.html', context)