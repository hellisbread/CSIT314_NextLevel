from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

from .models import Users, Reviewer, Paper, Bidded_Paper, Review, Comment

def reviewerPage(request):
    return render(request, 'reviewer/reviewer.html', {})