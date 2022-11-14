from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Users, Author, ConferenceChair, Reviewer, SystemAdmin

# log in page
def index(request):
    return render(request, 'index.html', {})

def checkLogin(request):

    if(request.POST):

        selectedRole = request.POST['roleList']

        print(selectedRole)

        username = request.POST['username']
        password = request.POST['password']

        if(selectedRole == "Author"):
            author = Author.getAuthor(username, password)

            if(author!=None):

                request.session['AuthorLogged'] = author.id

                #Redirects to author index
                return redirect('authorViewPaper')

            else:
                messages.error(request, "Invalid username or password.")
                return redirect('index')
            
        elif(selectedRole == "Reviewer"):

            reviewer = Reviewer.getReviewer(username, password)

            if(reviewer!=None):

                request.session['ReviewerLogged'] = reviewer.id

                return redirect('biddedPaper') #TOBEUPDATED

            else:
                messages.error(request, "Invalid username or password.")
                return redirect('index')

        elif(selectedRole == "Conference Chair"):
            Conf = ConferenceChair.getConferenceChair(username, password)

            if(Conf!=None):

                request.session['ConfLogged'] = Conf.id

                return redirect('allocationPaper') #TOBEUPDATED

            else:
                messages.error(request, "Invalid username or password.")
                return redirect('index')
        elif(selectedRole == "System Admin"):
            SysAdmin = SystemAdmin.getSystemAdmin(username, password)

            if(SysAdmin!=None):

                request.session['SysAdminLogged'] = SysAdmin.id

                return redirect('systemAdminPage') #TOBEUPDATED

            else:
                messages.error(request, "Invalid username or password.")
                return redirect('index')

    return redirect('index')