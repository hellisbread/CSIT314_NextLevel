from django.shortcuts import render, redirect

def systemAdminPage(request):

    return render(request, 'systemAdmin.html', {})

