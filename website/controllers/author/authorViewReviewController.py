from django.shortcuts import render
from ...models import Review, Paper

def viewReview(request, id):
    
    context = Review.getReviewAndPaperInfo(id)

    return render(request, 'author/viewReview.html', context)