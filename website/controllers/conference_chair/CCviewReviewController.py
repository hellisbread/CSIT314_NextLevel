
from django.shortcuts import render
from ...models import Review, Paper
from django.db.models import Q

from django.contrib import messages

def viewReview(request, id):
    reviews = Review.getAllReviewByPaperID(id)
    if reviews.count() > 0:
        paper = Paper.getPaper(id)
        text = paper.saved_file.read().decode("utf-8")
        context = {'reviews' : reviews, 'paper': paper, 'content':text}

        return render(request, 'conferenceChair/viewReview.html', context)
    else:
         # accept and reject table
        papers = Paper.objects.filter(status="Not Accessed").all()

        paperWithReview_list = Review.getAllPaperID()
        print(paperWithReview_list)
        # reviewExist = []
        # for paper in papers:
        #     if paper.id in paper_list:
        #         reviewExist.append(True)
        #     else:
        #         reviewExist.append(False)
        # decision table
        papers_decided = Paper.objects.filter(~Q(status="Not Accessed"))

        context = {'papers':papers, 'papers_decided':papers_decided, 'paperWithReview_list' : paperWithReview_list}

        messages.error(request, f"There is no review on paper ID {id} currently")
        return render(request, 'conferenceChair/acceptOrReject.html',context)

