from django.shortcuts import render, redirect
# from ...models import Author, Paper
from ...models import * # TO BE DELETED

from django.contrib import messages

def viewPaper(request):
    logged_author = str(request.session['AuthorLogged'])
    
    paper_list = Paper.getAllPaperByAuthorID(logged_author)
  
    context = {'papers' : paper_list, 'logged_author' : logged_author}

    return render(request, 'author/viewPaper.html', context)

def deleteSubmittedPaper(request, id):
    success = Paper.deleteSubmittedPaper(id)

    if(success):
        messages.success(request, f"Successfully delete paper ID {id}")
    else:
        messages.error(request, f"Fail to delete paper ID {id}")

    return redirect('authorViewPaper')