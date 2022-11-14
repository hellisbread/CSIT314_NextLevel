from django.shortcuts import render, redirect
from ...forms import UploadFileForm
from ...models import Author, Paper

from django.contrib import messages

def submitPaper(request):
    author_id = request.session['AuthorLogged']
    if request.method == 'POST':

        # collecting data from user input
        form = UploadFileForm(request.POST, request.FILES)
        topic = request.POST['topic']
        description = request.POST['description']
        file = request.FILES['file']
        authors = request.POST.getlist('authors')
        authors.append(author_id)

        success = Paper.createPaper(topic, description, str(file), file, authors, author_id)

        if(success):
            messages.success(request, "Successfully created Paper.")
        else:
            messages.error(request, "Invalid input found. Please ensure all fields are filled.")

        return redirect('authorViewPaper')

    else:
        form = UploadFileForm()
        authors = Author.getAllActiveAuthorWithoutLoggedAuthor(author_id)

    return render(request, 'author/submitPaper.html', {'form': form, 'authors': authors})