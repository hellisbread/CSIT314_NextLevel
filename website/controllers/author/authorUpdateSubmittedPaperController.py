from django.shortcuts import render, redirect
from ...forms import UpdateFileForm
from ...models import Author, Paper

from django.contrib import messages

def updateSubmittedPaper(request, id):
    paper = Paper.getPaper(id)
    author_id = int(paper.uploaded_by)
    logged_author = int(request.session['AuthorLogged'])

    if request.method == 'POST':
        # collecting data from user input
        form = UpdateFileForm(request.POST, request.FILES)
        new_topic = request.POST['topic']
        new_description = request.POST['description']
        new_authors = request.POST.getlist('authors')

        new_fileLocation = request.FILES.get('updatefile', False)

        new_fileName = str(new_fileLocation)


        if(new_fileLocation == False):
            new_fileName = paper.fileName
            new_fileLocation = paper.saved_file

        if len(new_authors) == 0:
            new_authors = paper.getAllAuthorID() 
        else:
            new_authors.append(author_id)

        success = paper.updatePaper(new_topic, new_description, new_fileName, new_fileLocation, new_authors)
    
        if(success):
            messages.success(request, "Successfully updated Paper.")
        else:
            messages.error(request, "Invalid input found. Please ensure all fields are filled.")

        return redirect('authorViewPaper')
    else:
        form = UpdateFileForm()
        authors = Author.getAllActiveAuthorWithoutLoggedAuthor(author_id)

        if int(logged_author) == int(author_id):
            co_author = "True"
        else:
            co_author = "False"

        return render(request, 'author/updateSubmittedPaper.html', {'form': form, 'authors': authors, 'paper' : paper, 'co_author': co_author})