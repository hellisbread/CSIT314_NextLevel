from django.shortcuts import render, redirect
from ...models import Bidded_Paper, Paper, Reviewer
from django.contrib import messages

def allocationPaper(request):
    # unallocate
    if request.method == 'POST':
        paper_id = request.POST['paper_id']
        reviewer_id = request.POST['reviewer_id']
        bidded_paper = Bidded_Paper.getAssignedPaperByPaperIDAndReviewerID(paper_id, reviewer_id)
        success = bidded_paper.updateStatus(0)
        if(success):
            messages.success(request, "successfully unallocated")
        else:
            messages.error(request, "unsucessfully unallocate")
        
    # need to be allocated table
    unassigned_paper_id_list = Bidded_Paper.getAllUnassignedPaperID()

    for paper_id in unassigned_paper_id_list:
        reviewer = []
        unassigned_reviewer_id_list = Bidded_Paper.getAllUnassignedReviewerID(paper_id)
        for reviewer_id in unassigned_reviewer_id_list:
            reviewer.append(reviewer_id['reviewer_id'])
        paper_id['reviewer'] = reviewer
    print(unassigned_paper_id_list)

    # allocated table
    assigned_paper_id_list = Bidded_Paper.getAllAssignedPaperID()
    for paper_id in assigned_paper_id_list:
        reviewer = []
        assigned_reviewer_id_list = Bidded_Paper.getAllAssignedReviewerID(paper_id['paper_id'])
        for reviewer_id in assigned_reviewer_id_list:
            reviewer.append(reviewer_id['reviewer_id'])
        paper_id['reviewer'] = reviewer

    context = {'unassigned_paper_id_list': unassigned_paper_id_list, 'assigned_paper_id_list': assigned_paper_id_list}
    
    return render(request, 'conferenceChair/allocationPaper.html', context)

def allocatePaper(request, id):
    if request.method == 'POST':
        paper_id = id
        reviewer_id = request.POST['chosenReviewerID']
        
        # check if number of paper < max paper
        maxPaper = Reviewer.getMaxPaperByID(reviewer_id)
        numOfPaperAssigned = Bidded_Paper.getNumberOfAssignedPaperByReviewerID(reviewer_id)


        if numOfPaperAssigned < maxPaper:
            bidded_papers = Bidded_Paper.getPaperByPaperIDAndReviewerID(paper_id, reviewer_id)
            for bidded_paper in bidded_papers:
                success = bidded_paper.updateStatus(1)
                if(success):
                    messages.success(request, "successfully assigned.")
                else:
                    messages.error(request, "unsucessfully assigned.")
        else:
            messages.error(request, "The number of paper for this reviewer has reached maximum!")

        return redirect('CCallocationPaper')
    else:
        reviewer_id_list = Bidded_Paper.getAllReviewerIDunassignedPaper(id)

        paper = Paper.getPaper(id=id)
        context = {'paper': paper, 'reviewer_id_list': reviewer_id_list}
        return render(request, 'conferenceChair/allocatePaper.html', context)