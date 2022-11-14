
from django.shortcuts import render
from ...models import Review, Paper
from django.db.models import Q

from django.contrib import messages

def viewReview(request, id):
    reviews = Review.getAllReviewByPaperID(id)
    if reviews.count() > 0:
        paper = Paper.getPaper(id)
        text = Paper.readSubmittedPaper(id)
        context = {'reviews' : reviews, 'paper': paper, 'content':text}

        return render(request, 'conferenceChair/viewReview.html', context)
    else:
        # accept and reject table
        papers = Paper.getAllNotAccessedPaper()

        paperWithReview_list = Review.getAllPaperID()
        papers_decided = Paper.getAllAcceptedRejectedPaper()

        messages.error(request, f"There is no review on paper ID {id} currently")
        context = {'papers':papers, 'papers_decided':papers_decided, 'paperWithReview_list' : paperWithReview_list}
        
        return render(request, 'conferenceChair/acceptOrReject.html',context)

