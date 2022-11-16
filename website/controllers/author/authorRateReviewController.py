from django.shortcuts import render, redirect
from ...models import Review, ReviewRating, Paper, Author, Reviewer

from django.contrib import messages

def rateReview(request):
    author_id = request.session["AuthorLogged"]

    # rate review
    final_review_list = Review.getAllUnReviewedByAuthorReviewsByAuthorID(author_id)

    # view rated review
    finalReviewRating_list = ReviewRating.getAllReviewRatingByAuthorID(author_id)

    context = {'final_review_list': final_review_list, 'finalReviewRating_list': finalReviewRating_list, 'loggedAuthor': author_id}
    
    return render(request, 'author/rateReview.html', context)

def CreateReview(request):
    if request.method == "POST":
        author_id = request.session["AuthorLogged"]

        review_id = request.POST["review_id"]
        paper_id = request.POST["paper_id"]
        reviewer_id = request.POST["reviewer_id"]
        rating = request.POST["rating"]

        success = ReviewRating.createReviewRating(review_id, paper_id, reviewer_id, author_id, rating)
        
        if(success):
            messages.success(request, "Successfully submitted your rating. Thank you for your submission.")
            return redirect('authorRateReview')
        else:
            messages.error(request, "There was an error submitting your rating.")
            return redirect('authorRateReview')


def deleteReviewRating(request, id):
    success = ReviewRating.deleteReviewRating(id)

    if(success):
        messages.success(request, f"Successfully delete reviewRating ID {id}")
    else:
        messages.error(request, f"Fail to delete reviewRating ID {id}")

    return redirect('authorRateReview')