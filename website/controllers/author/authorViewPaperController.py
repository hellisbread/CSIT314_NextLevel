from django.shortcuts import render, redirect
# from ...models import Author, Paper
from ...models import * # TO BE DELETED

from django.contrib import messages

def viewPaper(request):
    ### DEBUGGING ###
    paper_list = Paper.objects.all()
    for paper in paper_list:
        print(f'Paper ID: {paper.id}, Uploaded by: {paper.uploaded_by}, co-author: {paper.authors.all()}')

    review_list = Review.objects.all()
    for review in review_list:
        print(f'review ID: {review.id}, reviewer ID: {review.reviewer}, paper ID: {review.paper}')

    reviewRating_list = ReviewRating.objects.all()
    for reviewRating in reviewRating_list:
        print(f'reviewRating ID: {reviewRating.id}, reviewer ID: {reviewRating.reviewer}, paper ID: {reviewRating.paper}, author ID: {reviewRating.author}')


    ### END OF DEBUG MODE ###
    logged_author = str(request.session['AuthorLogged'])
    # paper_list = Paper.objects.all().filter(authors__in=[logged_author])
    paper_list = Paper.viewPaper(logged_author)
  
    context = {'papers' : paper_list, 'logged_author' : logged_author}

    return render(request, 'author/viewPaper.html', context)

def deleteSubmittedPaper(request, id):
    success = Paper.deleteSubmittedPaper(id)

    if(success):
        messages.success(request, f"Successfully delete paper ID {id}")
    else:
        messages.error(request, f"Fail to delete paper ID {id}")

    return redirect('authorViewPaper')