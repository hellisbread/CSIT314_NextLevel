from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

from website.models import Reviewer, Paper, Bidded_Paper

def bidPaper(request):

    reviewer_id = request.session['ReviewerLogged']

    paper_list = Paper.getAllUnbiddedPaper(reviewer_id)

    unassigned_list = Bidded_Paper.getAllUnassignedPaperByID(reviewer_id)

    context = {'papers':paper_list, 'unassigned_list':unassigned_list}

    return render(request, 'reviewer/bid_paper.html', context)

def addBidPaper(request, id):

    reviewer_id = request.session['ReviewerLogged']

    success = Bidded_Paper.createBiddedPaper(reviewer_id, id, "0")

    if(success):
        messages.success(request, "Successfully bidded for paper")
        return redirect('bidPaper')
    else:
        messages.error(request, "An error has occured while adding paper")

    return redirect('bidPaper')

def deleteBidPaper(request, id):

    reviewer_id = request.session['ReviewerLogged']

    success = Bidded_Paper.deleteBiddedPaperByID(id)

    if(success):
        messages.success(request, "You have successfully deleted your bid.")
        return redirect('bidPaper')
    else:
        messages.error(request, "This bid can no longer be deleted.")
        return redirect('bidPaper')
