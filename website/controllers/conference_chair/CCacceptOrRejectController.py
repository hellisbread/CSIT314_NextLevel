from django.shortcuts import render, redirect
from ...models import  Paper, Author, Review
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail

def acceptOrReject(request):

    context = Paper.getAllPaperAndReviews()

    return render(request, 'conferenceChair/acceptOrReject.html', context)

def acceptPaper(request):
    if request.method == 'POST':
        paper_id = request.POST['paper_id']

        success = Paper.updateStatusToAccepted(paper_id)

        if(success):
            messages.success(request, "Successfully accepted paper.")
            return redirect('CCacceptOrReject')

def rejectPaper(request):
    if request.method == 'POST':
        paper_id = request.POST['paper_id']

        success = Paper.updateStatusToRejected(paper_id)

        if(success):
            messages.success(request, "Successfully rejected paper.")
            return redirect('CCacceptOrReject')

def cancelDecision(request):
    if request.method == 'POST':
        paper_id = request.POST['paper_id']

        success = Paper.updateStatusToNotAccessed(paper_id)

        if(success):
            messages.success(request, "Successfully cancelled paper.")
            return redirect('CCacceptOrReject')

