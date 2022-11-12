from django.shortcuts import render, redirect
from .models import Bidded_Paper, Paper, Reviewer, Author
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail

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
            messages.error(request, "unsucessfully unallocate")
        
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
        print(reviewer)

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
        reviewer_id_list = Bidded_Paper.objects.filter(status=0).filter(paper_id=id).values_list('reviewer_id').distinct()

        paper = Paper.getPaper(id=id)
        context = {'paper': paper, 'reviewer_id_list': reviewer_id_list}
        return render(request, 'conferenceChair/allocatePaper.html', context)

def acceptOrReject(request):
    if request.method == 'POST':
        paper_id = request.POST['paper_id']
        paper = Paper.getPaper(paper_id)
        if request.POST.get("accept"):
            author_id_list = paper.authors.all().values_list('id', flat=True)
            success = paper.updateStatus("Accepted")
            for author_id in author_id_list:
                author_email = Author.getAuthorEmail(author_id)
                content = f'Dear Author ID {author_id}, your paper with ID {paper_id} is accepted. Thank you.'
                send_mail('Acceptation of Paper',
                content, 
                'nextlevelt05@gmail.com', 
                [author_email], 
                fail_silently=False)
                messages.success(request, f"Successfully send the email to Author ID {author_id}")
        elif request.POST.get("reject"):
            author_id_list = paper.authors.all().values_list('id', flat=True)
            success = paper.updateStatus("Rejected")
            for author_id in author_id_list:
                author_email = Author.getAuthorEmail(author_id)
                content = f'Dear Author ID {author_id}, your paper with ID {paper_id} is rejected. Thank you.'
                send_mail('Rejection of Paper',
                content, 
                'nextlevelt05@gmail.com', 
                [author_email], 
                fail_silently=False)
                messages.success(request, f"Successfully send the email to Author ID {author_id}")
        elif request.POST.get("cancel"):
            author_id_list = paper.authors.all().values_list('id', flat=True)
            success = paper.updateStatus("Not Accessed")
            for author_id in author_id_list:
                author_email = Author.getAuthorEmail(author_id)
                content = f'Dear Author ID {author_id}, the decision of you paper with ID {paper_id} is canceled. Thank you.'
                send_mail('Cancel decision of Paper',
                content, 
                'nextlevelt05@gmail.com', 
                [author_email], 
                fail_silently=False)
                messages.success(request, f"Successfully send the email to Author ID {author_id}")

    # accept and reject table
    papers = Paper.objects.filter(status="Not Accessed").all()

    # decision table
    papers_decided = Paper.objects.filter(~Q(status="Not Accessed"))

    context = {'papers':papers, 'papers_decided':papers_decided}

    return render(request, 'conferenceChair/acceptOrReject.html', context)

def readSubmittedPaper(request,id):
    paper = Paper.objects.get(id=id)
    text = paper.saved_file.read().decode("utf-8")

    context = {'content': text}

    return render(request, 'conferenceChair/readSubmittedPaper.html', context)

