from django.shortcuts import render
from .models import Bidded_Paper

def conferenceChairPage(request):
    return render(request, 'conferenceChair/conferenceChair.html',{})

def viewBiddedPaperPage(request):
    bid_list = Bidded_Paper.getAllBiddedPaper()
    context = {'bid_list':bid_list}

    return render(request, 'conferenceChair/viewBiddedPaper.html', context)
