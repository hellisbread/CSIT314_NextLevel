
from django.shortcuts import render
from ...models import Review, Paper
from django.db.models import Q

from django.contrib import messages

def viewReview(request, id):
    reviews = Review.getAllReviewByPaperID(id)
    if reviews.count() > 0:
        paper = Paper.getPaper(reviews[0].paper_id)
        text = paper.saved_file.read().decode("utf-8")
        context = {'reviews' : reviews, 'paper': paper, 'content':text}

        return render(request, 'conferenceChair/viewReview.html', context)
    else:
         # accept and reject table
        papers = Paper.objects.filter(status="Not Accessed").all()

        # decision table
        papers_decided = Paper.objects.filter(~Q(status="Not Accessed"))

        context = {'papers':papers, 'papers_decided':papers_decided}

        messages.error(request, f"There is no review on paper ID {id} currently")
        return render(request, 'conferenceChair/acceptOrReject.html',context)

