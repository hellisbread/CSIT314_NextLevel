from django.shortcuts import render
from ...models import Paper

def readSubmittedPaper(request, id):
    text = Paper.readSubmittedPaper(id)

    paper = Paper.getPaper(id)

    context = {'paper':paper, 'content': text}

    return render(request, 'author/readSubmittedPaper.html', context)
