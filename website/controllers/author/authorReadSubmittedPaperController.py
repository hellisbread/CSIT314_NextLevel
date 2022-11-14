from django.shortcuts import render
from ...models import Paper

def readSubmittedPaper(request, id):
    text = Paper.readSubmittedPaper(id)
    context = {'content': text}

    return render(request, 'author/readSubmittedPaper.html', context)
