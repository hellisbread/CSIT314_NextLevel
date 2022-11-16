from django.shortcuts import render, redirect
from django.contrib import messages

from website.models import Reviewer, Review, Comment

def commentPage(request, bid_id, id):
    reviewer_id = request.session['ReviewerLogged']

    context = Comment.getAllcommentPageDetails(id, reviewer_id, bid_id)

    return render(request, 'reviewer/comments.html', context)

def createComment(request, bid_id, id):

    if (request.POST):
        rating = request.POST['rating']
        description = request.POST['description']

        reviewer_id = request.session['ReviewerLogged']

        success = Comment.createComment(id, reviewer_id, rating, description)

        if(success):
            messages.success(request, "Your comment have been posted successfully.")
            return redirect('commentPage', bid_id = bid_id, id = id)
        else:
            messages.error(request, "There was an error posting your comment.")
            return redirect('commentPage',bid_id = bid_id, id = id)
    
def editComment(request, bid_id):

    if (request.POST):
        id = request.POST['review_id']
        comment_id = request.POST['comment_id']

        rating = request.POST['rating']
        description = request.POST['description']

        success = Comment.updateComment(comment_id, rating, description)

        if(success):
            messages.success(request, "Your comment has been updated.")
            return redirect('commentPage', bid_id = bid_id, id = id)
        else:
            messages.error(request, "There was an error updating your comment.")
            return redirect('commentPage', bid_id = bid_id, id = id)
    else:
        return redirect('index')

def deleteComment(request, bid_id, id, comment_id):

    success = Comment.deleteComment(comment_id)

    if(success):
        messages.success(request, "Your comment has been deleted.")
        return redirect('commentPage', bid_id = bid_id, id = id)
    else:
        messages.error(request, "There was an error deleting your comment.")
        return redirect('commentPage', bid_id = bid_id, id = id)