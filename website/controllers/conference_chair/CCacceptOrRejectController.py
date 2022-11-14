from django.shortcuts import render
from ...models import  Paper, Author, Review
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail

def acceptOrReject(request):
    if request.method == 'POST':
        paper_id = request.POST['paper_id']
        paper = Paper.getPaper(paper_id)
        author_id_list = paper.getAllAuthorID()
        if request.POST.get("accept"):
            # author_id_list = paper.authors.all().values_list('id', flat=True)
            success = paper.updateStatus("Accepted")
            for author_id in author_id_list:
                author_email = Author.getAuthorEmail(author_id)
                content = f'Dear Author ID {author_id}, your paper with ID {paper_id} is accepted. Thank you.'
                
                send_mail('Acceptation of Paper',
                content, 
                'nextlevelt05@gmail.com', 
                [author_email], 
                fail_silently=False)
                messages.success(request, f"Successfully send the email to Author ID {author_id}")

        elif request.POST.get("reject"):
            # author_id_list = paper.authors.all().values_list('id', flat=True)
            success = paper.updateStatus("Rejected")
            for author_id in author_id_list:
                author_email = Author.getAuthorEmail(author_id)
                content = f'Dear Author ID {author_id}, your paper with ID {paper_id} is rejected. Thank you.'
                
                send_mail('Rejection of Paper',
                content, 
                'nextlevelt05@gmail.com', 
                [author_email], 
                fail_silently=False)
                messages.success(request, f"Successfully send the email to Author ID {author_id}")

        elif request.POST.get("cancel"):
            # author_id_list = paper.authors.all().values_list('id', flat=True)
            success = paper.updateStatus("Not Accessed")
            for author_id in author_id_list:
                author_email = Author.getAuthorEmail(author_id)
                content = f'Dear Author ID {author_id}, the decision of you paper with ID {paper_id} is canceled. Thank you.'
                
                send_mail('Cancel decision of Paper',
                content, 
                'nextlevelt05@gmail.com', 
                [author_email], 
                fail_silently=False)
                messages.success(request, f"Successfully send the email to Author ID {author_id}")

    # accept and reject table
    papers = Paper.objects.filter(status="Not Accessed").all()

    paperWithReview_list = Review.getAllPaperID()

    # decision table
    papers_decided = Paper.objects.filter(~Q(status="Not Accessed"))
    
    context = {'papers':papers, 'papers_decided':papers_decided, 'paperWithReview_list' : paperWithReview_list}

    return render(request, 'conferenceChair/acceptOrReject.html', context)