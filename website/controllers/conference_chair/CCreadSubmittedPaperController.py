from django.shortcuts import render
from ...models import Paper

def readSubmittedPaper(request,id):
    paper = Paper.getPaper(id)
    text = Paper.readSubmittedPaper(id)

    context = {'paper': paper, 'content': text}

    return render(request, 'conferenceChair/readSubmittedPaper.html', context)
