from django.shortcuts import render
from ...models import Review, Paper

def viewReview(request, id):
    review = Review.getReview(id)
    paper = Paper.getPaper(review.paper_id)
    print(paper.topic)
    
    text = paper.getText()

    context = {'review': review, 'paper' : paper, 'content': text}

    return render(request, 'author/viewReview.html', context)