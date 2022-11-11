from django.shortcuts import render, redirect
from .models import Bidded_Paper, Paper, Reviewer
from django.contrib import messages
from django.db.models import Q

def conferenceChairPage(request):
    return render(request, 'conferenceChair/conferenceChair.html',{})

def allocationPaper(request):
    # allocated table
    if request.method == 'POST':
        paper_id = request.POST['paper_id']
        reviewer_id = request.POST['reviewer_id']
        bidded_paper = Bidded_Paper.objects.filter(status=1).filter(paper_id=paper_id).filter(reviewer_id=reviewer_id)
        success = bidded_paper[0].updateStatus(0)
        if(success):
            messages.success(request, "successfully unallocated")
        else:
            messages.error(request, "unsucessfully unallocated")
        
    # need to be allocated table
    paper_id_list_not_allocate = Bidded_Paper.objects.all().filter(status=0).values('paper_id').distinct()
    for paper_id in paper_id_list_not_allocate:
        reviewer = []
        reviewer_id_list_not_allocate = Bidded_Paper.objects.filter(status=0).filter(paper_id=paper_id['paper_id']).values('reviewer_id').distinct()
        for reviewer_id in reviewer_id_list_not_allocate:
            reviewer.append(reviewer_id['reviewer_id'])
        paper_id['reviewer'] = reviewer

    # allocated table
    paper_id_list_allocated = Bidded_Paper.objects.all().filter(status=1).values('paper_id').distinct()
    for paper_id in paper_id_list_allocated:
        reviewer = []
        reviewer_id_list_allocated = Bidded_Paper.objects.filter(status=1).filter(paper_id=paper_id['paper_id']).values('reviewer_id').distinct()
        for reviewer_id in reviewer_id_list_allocated:
            reviewer.append(reviewer_id['reviewer_id'])
        paper_id['reviewer'] = reviewer

    context = {'paper_id_list_not_allocate': paper_id_list_not_allocate, 'paper_id_list_allocated': paper_id_list_allocated}

    return render(request, 'conferenceChair/allocationPaper.html', context)

def allocatePaper(request, id):
    if request.method == 'POST':
        paper_id = id
        reviewer_id = request.POST['chosenReviewerID']
        
        # check if number of paper < max paper
        maxPaper = Reviewer.getMaxPaperByID(reviewer_id)
        numOfPaperAssigned = Bidded_Paper.objects.filter(status=1).filter(reviewer_id = reviewer_id).count()

        if numOfPaperAssigned < maxPaper:
            bidded_papers = Bidded_Paper.objects.filter(paper_id=paper_id).filter(reviewer_id=reviewer_id)
            for bidded_paper in bidded_papers:
                success = bidded_paper.updateStatus(1)
                if(success):
                    messages.success(request, "successfully assigned.")
                else:
                    messages.error(request, "unsucessfully assigned.")
        else:
            messages.error(request, "The number of paper for this reviewer has reached maximum!")

        return redirect('allocationPaper')
    else:
        reviewer_id_list = Bidded_Paper.objects.filter(paper_id=id).values_list('reviewer_id').distinct()

        paper = Paper.objects.get(id=id)
        context = {'paper': paper, 'reviewer_id_list': reviewer_id_list}
        return render(request, 'conferenceChair/allocatePaper.html', context)

def acceptOrReject(request):
    if request.method == 'POST':
        paper_id = request.POST['paper_id']
        paper = Paper.getPaper(paper_id)
        if request.POST.get("accept"):
            success = paper.updateStatus("Accepted")
        elif request.POST.get("reject"):
            success = paper.updateStatus("Rejected")
        elif request.POST.get("cancel"):
            success = paper.updateStatus("Not Accessed")

    # accept and reject table
    papers = Paper.objects.filter(status="Not Accessed").all().values()

    # decision table
    papers_decided = Paper.objects.filter(~Q(status="Not Accessed"))

    context = {'papers':papers, 'papers_decided':papers_decided}

    return render(request, 'conferenceChair/acceptOrReject.html', context)

def decidePaper(request, id):
    if request.method == 'POST':
        decision = request.POST['decision']
        print(decision)
        paper = Paper.objects.get(id=id)
        context = {'paper': paper}
        return render(request,'conferenceChair/decidePaper.html', context)
    else:
        paper = Paper.objects.get(id=id)
        context = {'paper': paper}
        return render(request,'conferenceChair/decidePaper.html', context)

def readSubmittedPaper(request,id):
    paper = Paper.objects.get(id=id)
    text = paper.saved_file.read().decode("utf-8")

    context = {'content': text}

    return render(request, 'conferenceChair/readSubmittedPaper.html', context)

