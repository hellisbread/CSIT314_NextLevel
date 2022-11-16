from django.shortcuts import render, redirect
from ...models import Bidded_Paper, Paper, Reviewer
from django.contrib import messages

def allocatePaperPage(request, id):
    context = Bidded_Paper.getAllAllocatePaperDetails(id)
    
    return render(request, 'conferenceChair/allocatePaper.html', context)

def allocatePaper(request, id):
    if request.method == 'POST':
        reviewer_id = request.POST['chosenReviewerID']

        success = Bidded_Paper.updateStatusToAllocated(id, reviewer_id)
        
        if(success == "Success"):
            messages.success(request, "Successfully allocated paper to reviewer")
            return redirect('CCallocationPaper')
        elif(success == "Error 1"):
            messages.error(request, "Failed to allocate paper.")
            return redirect('CCallocatePaperPage', id=id)
        elif(success == "Error 2"):
            messages.error(request, "Failed to allocate paper due to max paper limited")
            return redirect('CCallocatePaperPage', id=id)

        
