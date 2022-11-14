from django.shortcuts import render, redirect
from ...models import Review, ReviewRating, Paper, Author, Reviewer

from django.contrib import messages

def rateReview(request):
    author_id = request.session["AuthorLogged"]
    if request.method == "POST":
        paper = Paper.getPaper(request.POST["paper_id"])
        reviewer = Reviewer.getReviewerByID(request.POST["reviewer_id"])
        author = Author.getAuthorByID(author_id)
        rating = request.POST["rating"]
        success = ReviewRating.createReviewRating(paper, reviewer, author, rating)
        
        if(success):
            messages.success(request, "Successfully submitted your rating. Thank you for your submission.")
            return redirect('authorRateReview')
        else:
            messages.error(request, "There was an error submitting your rating.")
            return redirect('authorRateReview')
    else:
        # rate review
        review_list = Review.getAllReview()
        final_review_list = []
        
        for review in review_list:
            paper = Paper.getPaper(review.paper_id)
            author_list = paper.getAllAuthorID()
            authorHasNotReviewed = ReviewRating.checkAuthorHasNotReviewed(review.paper_id, review.reviewer_id, author_id)

            if author_id in author_list and authorHasNotReviewed:
                final_review_list.append(review)
            
        # view rated review
        reviewRating_list = ReviewRating.getAllReviewRating()
        finalReviewRating_list = []
        for reviewRating in reviewRating_list:
            paper = Paper.getPaper(reviewRating.paper_id)
            author_list = paper.getAllAuthorID()
            if author_id in author_list:
                finalReviewRating_list.append(reviewRating)

        context = {'final_review_list': final_review_list, 'finalReviewRating_list': finalReviewRating_list, 'loggedAuthor': author_id}
        return render(request, 'author/rateReview.html', context)

def deleteReviewRating(request, id):
    success = ReviewRating.deleteReviewRating(id)

    if(success):
        messages.success(request, f"Successfully delete reviewRating ID {id}")
    else:
        messages.error(request, f"Fail to delete reviewRating ID {id}")

    return redirect('authorRateReview')