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
            authorUser = Author.objects.filter(username = username, password=password)

            if(authorUser.exists()):
                author = Author.objects.get(username = username, password = password)

                request.session['AuthorLogged'] = author.username

                #Redirects to author index
                return redirect('db') #TOBEUPDATED

            else:
                messages.error(request, "Invalid username or password.")
                return redirect('index')
            
        elif(selectedRole == "Reviewer"):

            ReviewerUser = Reviewer.objects.filter(username = username, password=password)

            if(ReviewerUser.exists()):
                reviewer = Reviewer.objects.get(username = username, password = password)

                request.session['ReviewerLogged'] = reviewer.username

                return redirect('db') #TOBEUPDATED

            else:
                messages.error(request, "Invalid username or password.")
                return redirect('index')

        elif(selectedRole == "Conference Chair"):
            ConfUser = ConferenceChair.objects.filter(username = username, password=password)

            if(ConfUser.exists()):
                Conf = ConferenceChair.objects.get(username = username, password = password)

                request.session['ConfLogged'] = Conf.username

                return redirect('db') #TOBEUPDATED

            else:
                messages.error(request, "Invalid username or password.")
                return redirect('index')
        elif(selectedRole == "System Admin"):
            SysUser = SystemAdmin.objects.filter(username = username, password=password)

            if(SysUser.exists()):
                SysAdmin = SystemAdmin.objects.get(username = username, password = password)

                request.session['SysAdminLogged'] = SysAdmin.username

                return redirect('db') #TOBEUPDATED

            else:
                messages.error(request, "Invalid username or password.")
                return redirect('index')

    return redirect('index')