from django.shortcuts import render, redirect
from ...forms import UpdateFileForm
from ...models import Author, Paper

from django.contrib import messages

def updateSubmittedPaperPage(request, id):
    paper = Paper.getPaper(id)
    author_id = int(paper.uploaded_by)
    logged_author = int(request.session['AuthorLogged'])

    form = UpdateFileForm()
    authors = Author.getAllActiveAuthorWithoutLoggedAuthor(author_id)

    if int(logged_author) == int(author_id):
        co_author = "True"
    else:
        co_author = "False"

    return render(request, 'author/updateSubmittedPaper.html', {'form': form, 'authors': authors, 'paper' : paper, 'co_author': co_author})

def updateSubmittedPaper(request, id):
    if request.method == 'POST':
        new_topic = request.POST['topic']
        new_description = request.POST['description']
        new_authors = request.POST.getlist('authors')

        new_fileLocation = request.FILES.get('updatefile', False)

        success = Paper.updatePaper(id, new_topic, new_description, new_fileLocation, new_authors)
    
        if(success):
            messages.success(request, "Successfully updated Paper.")
            return redirect('authorViewPaper')
        else:
            messages.error(request, "Invalid input found. Please ensure all fields are filled.")
            return redirect('authorUpdateSubmittedPaper', id=id)