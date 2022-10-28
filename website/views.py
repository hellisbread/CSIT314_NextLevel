from django.shortcuts import redirect
from django.contrib import messages

from .models import *

# Create your views here.

def Logout(request):
    if 'AuthorLogged' in request.session:
        del request.session['AuthorLogged']

    if 'ReviewerLogged' in request.session:
        del request.session['ReviewerLogged']

    if 'ConfLogged' in request.session:
        del request.session['ConfLogged']

    if 'SysAdminLogged' in request.session:
        del request.session['SysAdminLogged']

    messages.success(request, "You have successfully logged out.")
    return redirect('index')

