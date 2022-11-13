from django.shortcuts import render, redirect
from django.contrib import messages

from website.models import Reviewer, Review, Comment

def commentPage(request, id):

    review = Review.getReview(id)

    comments = Comment.getAllCommentByReviewID(id)

    reviewer_id = request.session['ReviewerLogged']

    reviewer = Reviewer.getReviewerByID(reviewer_id)

    context = {'review':review , 'comments':comments, 'reviewer':reviewer}

    print(context)

    return render(request, 'reviewer/comments.html', context)

def createComment(request, id):

    if (request.POST):

        rating = request.POST['rating']
        description = request.POST['description']

        reviewer_id = request.session['ReviewerLogged']

        reviewer = Reviewer.getReviewerByID(reviewer_id)

        success = Comment.createComment(id, reviewer.name, rating, description)

        if(success):
            messages.success(request, "Your comment have been posted successfully.")
            return redirect('commentPage', id = id)
        else:
            messages.error(request, "There was an error posting your comment.")
            return redirect('commentPage', id = id)
    
def editComment(request):

    if (request.POST):
        id = request.POST['review_id']
        comment_id = request.POST['comment_id']

        rating = request.POST['rating']
        description = request.POST['description']

        success = Comment.updateComment(comment_id, rating, description)

        if(success):
            messages.success(request, "Your comment has been updated.")
            return redirect('commentPage', id = id)
        else:
            messages.error(request, "There was an error updating your comment.")
            return redirect('commentPage', id = id)
    else:
        return redirect('index')

def deleteComment(request, id, comment_id):

    success = Comment.deleteComment(comment_id)

    if(success):
        messages.success(request, "Your comment has been deleted.")
        return redirect('commentPage', id = id)
    else:
        messages.error(request, "There was an error deleting your comment.")
        return redirect('commentPage', id = id)