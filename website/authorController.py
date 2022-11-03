from django.shortcuts import render
from .forms import UploadFileForm
from .models import Author, Paper
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

def authorPage(request):
    return render(request, 'author/author.html', {'author_id': id})

def submitPaperPage(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        topic = request.POST['topic']
        description = request.POST['description']
        file = request.FILES['file']
        authors = request.POST.getlist('authors')
        success = Paper.createPaper(topic, description, str(file), file, authors)
        if(success):
            messages.success(request, "Successfully created Paper.")
        else:
            messages.error(request, "Invalid input found. Please ensure all fields are filled.")

        return HttpResponseRedirect(reverse('viewPaperPage'))

    else:
        form = UploadFileForm()
        authors = Author.getAllAuthor()
    return render(request, 'author/submitPaper.html', {'form': form, 'authors': authors})

def viewPaperPage(request):
    papers = Paper.objects.all()
    template = loader.get_template('author/viewPaper.html')
    context = {'papers' : papers}

    return HttpResponse(template.render(context, request))

def deleteSubmittedPaper(request, id):
    paper = Paper.objects.get(id=id)
    paper.delete()
    return HttpResponseRedirect(reverse('viewPaperPage'))

def readSubmittedPaper(request, id):
    paper = Paper.objects.get(id=id)
    template = loader.get_template('author/readSubmittedPaper.html')
    text = paper.saved_file.read().decode()

    body = {'content': text}

    return HttpResponse(template.render(body, request))

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

        return HttpResponseRedirect(reverse('viewPaperPage'))
    else:
        form = UploadFileForm()
        authors = Author.getAllAuthor()
        paper = Paper.objects.get(id=id)

    return render(request, 'author/updateSubmittedPaper.html', {'form': form, 'authors': authors, 'paper' : paper})