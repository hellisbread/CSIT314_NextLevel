
from django.shortcuts import render
from ...models import Review, Paper
from django.db.models import Q

from django.contrib import messages

def viewReview(request, id):

    context = Review.getAllReviewDetailsByPaperID(id)

    return render(request, 'conferenceChair/viewReview.html', context)