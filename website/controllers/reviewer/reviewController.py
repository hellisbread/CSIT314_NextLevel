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

def editReview(request, bid_id, id):
    if(request.POST):
        title = request.POST['title']
        description = request.POST['description']
        rating = request.POST['rating']

        reviewer_id = request.session['ReviewerLogged']

        success = Review.updateReview(id,rating,title,description)

        if(success):
            messages.success(request, "Successfully updated your review.")
            return redirect('reviewPaper', id = bid_id)
        else:
            messages.error(request, "There was an error updating your review.")
            return redirect('reviewPaper', id = bid_id)

    else:
        return redirect('reviewPaper', id = bid_id)

def deleteReview(request, bid_id, id):

    reviewer_id = request.session['ReviewerLogged']

    success = Review.deleteReviewByID(bid_id, id)

    if(success):

        messages.success(request, "Successfully deleted your review.")
        return redirect('reviewPaper', id = bid_id)
    else:
        messages.error(request, "An error has occured.")
        return redirect('reviewPaper', id = bid_id)
