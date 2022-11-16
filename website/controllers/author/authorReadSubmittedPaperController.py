from django.shortcuts import render
from ...models import Paper

def readSubmittedPaper(request, id):
    
    context = Paper.getPaperContent(id)

    return render(request, 'author/readSubmittedPaper.html', context)
