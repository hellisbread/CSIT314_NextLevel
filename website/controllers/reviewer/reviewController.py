from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

from website.models import Reviewer, Paper, Bidded_Paper, Review

def reviewPage(request, id):

    reviewer_id = request.session['ReviewerLogged']

    context = Review.getReviewPageDetails(reviewer_id, id)

    return render(request, 'reviewer/review_paper.html', context)

def createReview(request, id):
    if(request.POST):

        reviewer_id = request.session['ReviewerLogged']

        title = request.POST['title']
        description = request.POST['description']
        rating = request.POST['rating']

        success = Review.createReview(id, reviewer_id, rating, title, description)

        if(success):
            messages.success(request, "Successfully submitted your review. Thank you for your submission.")
            return redirect('reviewPaper', id = id)
        else:
            messages.error(request, "There was an error submitting your review.")
            return redirect('reviewPaper', id = id)
    else:
        return redirect('reviewPaper', id = id)

def editReview(request, id):
    if(request.POST):

        title = request.POST['title']
        description = request.POST['description']
        rating = request.POST['rating']

        bidPaper = Bidded_Paper.getBiddedPaper(id)

        paper = Paper.getPaper(bidPaper.paper_id)

        reviewer_id = request.session['ReviewerLogged']

        review = Review.getReviewByPaperAndReviewer(bidPaper.paper_id, reviewer_id)

        success = Review.updateReview(review.id,rating,title,description)

        if(success):
            messages.success(request, "Successfully updated your review.")
            return redirect('reviewPaper', id = id)
        else:
            messages.error(request, "There was an error updating your review.")
            return redirect('reviewPaper', id = id)

    else:
        return redirect('reviewPaper', id = id)

def deleteReview(request, id):

    bidPaper = Bidded_Paper.getBiddedPaper(id)

    reviewer_id = request.session['ReviewerLogged']

    review = Review.getReviewByPaperAndReviewer(bidPaper.paper_id, reviewer_id)

    if(review!=None):
        review.deleteReview()

        bidPaper.updateStatus("1")
        messages.success(request, "Successfully deleted your review.")
        return redirect('reviewPaper', id = id)
    else:
        messages.error(request, "An error has occured.")
        return redirect('reviewPaper', id = id)
