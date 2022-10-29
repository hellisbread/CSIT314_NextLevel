from django.shortcuts import render, redirect

def authorPage(request):

    return render(request, 'author.html', {})

    
def submitPaperPage(request):

    return render(request, 'submitPaper.html', {})