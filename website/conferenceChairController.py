from django.shortcuts import render, redirect
from .models import Bidded_Paper, Paper
from django.contrib import messages

def conferenceChairPage(request):
    return render(request, 'conferenceChair/conferenceChair.html',{})

def viewBiddedPaperPage(request):
    paper_id_list_not_allocate = Bidded_Paper.objects.all().filter(status=0).values('paper_id').distinct()
    
    for paper_id in paper_id_list_not_allocate:
        reviewer = []
        reviewer_id_list_not_allocate = Bidded_Paper.objects.filter(status=0).filter(paper_id=paper_id['paper_id']).values('reviewer_id').distinct()
        
        for reviewer_id in reviewer_id_list_not_allocate:
            reviewer.append(reviewer_id['reviewer_id'])
        paper_id['reviewer'] = reviewer

    paper_id_list_allocated = Bidded_Paper.objects.all().filter(status=1).values('paper_id').distinct()
    
    for paper_id in paper_id_list_allocated:
        reviewer = []
        reviewer_id_list_allocated = Bidded_Paper.objects.filter(status=1).filter(paper_id=paper_id['paper_id']).values('reviewer_id').distinct()
        
        for reviewer_id in reviewer_id_list_allocated:
            reviewer.append(reviewer_id['reviewer_id'])
        paper_id['reviewer'] = reviewer

    context = {'paper_id_list_not_allocate': paper_id_list_not_allocate, 'paper_id_list_allocated': paper_id_list_allocated}

    return render(request, 'conferenceChair/viewBiddedPaper.html', context)

def allocatePaper(request, id):
    if request.method == 'POST':
        paper_id = id
        reviewer_id = request.POST['chosenReviewerID']
        bidded_papers = Bidded_Paper.objects.filter(paper_id=paper_id).filter(reviewer_id=reviewer_id)
        for bidded_paper in bidded_papers:
            success = bidded_paper.updateStatus(1)
            if(success):
                messages.success(request, "successfully assigned.")
            else:
                messages.error(request, "unsucessfully assigned.")

        return redirect('viewBiddedPaperPage')
    else:
        reviewer_id_list = Bidded_Paper.objects.filter(paper_id=id).values_list('reviewer_id').distinct()

        paper = Paper.objects.get(id=id)
        context = {'paper': paper, 'reviewer_id_list': reviewer_id_list}
        return render(request, 'conferenceChair/allocatePaper.html', context)

