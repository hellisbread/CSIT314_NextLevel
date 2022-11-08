from django.shortcuts import render
from .models import Bidded_Paper

def conferenceChairPage(request):
    return render(request, 'conferenceChair/conferenceChair.html',{})

def viewBiddedPaperPage(request):
    paper_id_list = Bidded_Paper.objects.all().values('paper_id').distinct()
    
    for paper_id in paper_id_list:
        candidate = []
        reviewer_id_list = Bidded_Paper.objects.filter(paper_id=paper_id['paper_id']).values('reviewer_id').distinct()
        
        for reviewer_id in reviewer_id_list:
            candidate.append(reviewer_id['reviewer_id'])
        paper_id['candidate'] = candidate

    context = {'paper_id_list': paper_id_list}

    return render(request, 'conferenceChair/viewBiddedPaper.html', context)
