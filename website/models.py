from asyncio.windows_events import NULL
from audioop import maxpp
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Users(models.Model):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(max_length = 255, unique=True)
    password = models.CharField(max_length = 255)
    #verified = models.BooleanField(default = False)
    #approved = models.BooleanField(default = False)

    class Meta:
        db_table = 'user'

    @classmethod
    def createUser(cls, email, username, password, Name):

        if(email.replace(" ","")=="" or username.replace(" ","") == "" or password.replace(" ","") == "" or Name.replace(" ","") == ""):
            return False

        newUser = cls(email=email, username=username,password=password,Name = Name)

        newUser.save()

        return True

    def updateUser(self, email, username, password, Name):
        return self

class SystemAdmin(Users):

    class Meta(User.Meta):
        db_table = 'system_admin'

    @classmethod
    def createSystemAdmin(cls, email, username, password):

        if(email.replace(" ","")=="" or username.replace(" ","") == "" or password.replace(" ","") == ""):
            return False

        newSystemAdmin= cls(email = email, username=username, password=password)

        newSystemAdmin.save()

        return True

class Author(Users):
    Name = models.CharField(max_length = 255)

    class Meta(User.Meta):
        db_table = 'author'

    @classmethod
    def createAuthor(cls, email, username, password, Name):

        if(email.replace(" ","")=="" or username.replace(" ","") == "" or password.replace(" ","") == "" or Name.replace(" ","") == ""):
            return False

        newAuthor = cls(email = email, username=username, password=password, Name = Name)

        newAuthor.save()

        return True

class Reviewer(Users):
    maxPaper = models.IntegerField(default = 0)
    Name = models.CharField(max_length = 255)

    class Meta(User.Meta):
        db_table = 'reviewer'

    @classmethod
    def createReviewer(cls, email, username, password, Name, maxPaper):

        if(email.replace(" ","")=="" or username.replace(" ","") == "" or password.replace(" ","") == "" or Name.replace(" ","") == ""or maxPaper.replace(" ","") == ""):
            return False

        newReviewer = cls(email = email, username=username, password=password, Name = Name, maxPaper = maxPaper)

        newReviewer.save()

        return True

class ConferenceChair(Users):
    Name = models.CharField(max_length = 255)

    class Meta(User.Meta):
        db_table = 'conference_chair'

    @classmethod
    def CreateConferenceChair(cls, email, username, password, Name):

        newConfChair = cls(email = email, username=username, password=password, Name = Name)

        newConfChair.save()

        return True






