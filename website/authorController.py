from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import Author, Paper

from django.contrib import messages

def authorPage(request):
    return render(request, 'author/author.html', {'author_id': id})

def submitPaperPage(request):
    author_id = request.session['AuthorLogged']
    if request.method == 'POST':
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

        return redirect('viewPaperPage')

    else:
        form = UploadFileForm()
        authors = Author.getAllActiveAuthor().exclude(id=author_id)

    return render(request, 'author/submitPaper.html', {'form': form, 'authors': authors})

def viewPaperPage(request):
    author_id = request.session['AuthorLogged']
    paper_list = Paper.objects.all().filter(authors__in=[author_id])

    context = {'papers' : paper_list}

    return render(request, 'author/viewPaper.html', context)

def deleteSubmittedPaper(request, id):
    paper = Paper.objects.get(id=id)
    paper.delete()
    return redirect('viewPaperPage')

def readSubmittedPaper(request, id):
    paper = Paper.objects.get(id=id)
    text = paper.saved_file.read().decode("utf-8")

    context = {'content': text}

    return render(request, 'author/readSubmittedPaper.html', context)

def updateSubmittedPaper(request, id):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        new_topic = request.POST['topic']
        new_description = request.POST['description']
        new_file = request.FILES['file']
        new_authors = request.POST.getlist('authors')
        paper = Paper.objects.get(id=id)

        success = paper.updatePaper(new_topic, new_description, str(new_file), new_file, new_authors)
    
        if(success):
            messages.success(request, "Successfully updated Paper.")
        else:
            messages.error(request, "Invalid input found. Please ensure all fields are filled.")

        return redirect('viewPaperPage')
    else:
        form = UploadFileForm()
        authors = Author.getAllAuthor()
        paper = Paper.objects.get(id=id)

    return render(request, 'author/updateSubmittedPaper.html', {'form': form, 'authors': authors, 'paper' : paper})