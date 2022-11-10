from django.template import loader
from django.contrib import messages

from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import validate_email

from .models import Users, Author, ConferenceChair, Reviewer, SystemAdmin



     