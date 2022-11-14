
from django.shortcuts import render
from ...models import Review, Paper

def viewReview(request, id):
    reviews = Review.getAllReviewByPaperID(id)
    paper = Paper.getPaper(reviews[0].paper_id)
    text = paper.saved_file.read().decode("utf-8")
    context = {'reviews' : reviews, 'paper': paper, 'content':text}

    return render(request, 'conferenceChair/viewReview.html', context)