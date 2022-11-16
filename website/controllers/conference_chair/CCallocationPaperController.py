from django.shortcuts import render, redirect
from ...models import Bidded_Paper, Paper, Reviewer
from django.contrib import messages

def allocationPaperPage(request):
    unassigned_paper_id_list = Bidded_Paper.GetAllUnassignedPapers()

    # allocated table
    assigned_paper_id_list = Bidded_Paper.getAllAssignedPapers()

    context = {'unassigned_paper_id_list': unassigned_paper_id_list, 'assigned_paper_id_list': assigned_paper_id_list}
    
    return render(request, 'conferenceChair/allocationPaper.html', context)

def unallocatePaper(request):
    if request.method == 'POST':
        paper_id = request.POST['paper_id']
        reviewer_id = request.POST['reviewer_id']

        success = Bidded_Paper.updateStatusToUnallocate(paper_id, reviewer_id)

        if(success):
            messages.success(request, "successfully unallocated")
            return redirect('CCallocationPaper')
        else:
            messages.error(request, "unsucessfully unallocate")
            return redirect('CCallocationPaper')

def autoAllocate(request):
    if request.method == 'POST':

        success = Bidded_Paper.AutoAllocate()

        if(success):
            messages.success(request, "Successfully allocate paper automatically!")
            return redirect('CCallocationPaper')
        else:
            messages.error(request, "There was an error allocating.")
            return redirect('CCallocationPaper')

    

        