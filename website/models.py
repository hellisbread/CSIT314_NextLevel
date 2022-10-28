from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

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

    #Get specific system admin user
    def getSystemAdmin(username, password):
        try:
            systemAdmin = SystemAdmin.objects.get(username=username,password=password)

            return systemAdmin
        except (SystemAdmin.DoesNotExist, ObjectDoesNotExist):
            return None

    #Get All System Admins
    def getAllSystemAdmin():
        system_list = SystemAdmin.objects.all().values()

        return system_list

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

    #Get specific author user
    def getAuthor(username, password):
        try:
            author = Author.objects.get(username=username,password=password)

            return author
        except (Author.DoesNotExist, ObjectDoesNotExist):
            return None
    
    def getAllAuthor():
        author_list = Author.objects.all().values()

        return author_list

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

    def getReviewer(username, password):
        try:
            reviewer = Reviewer.objects.get(username=username,password=password)

            return reviewer
        except (Reviewer.DoesNotExist, ObjectDoesNotExist):
            return None
    
    def getAllReviewer():
        reviewer_list = Reviewer.objects.all().values()

        return reviewer_list
    

class ConferenceChair(Users):
    Name = models.CharField(max_length = 255)

    class Meta(User.Meta):
        db_table = 'conference_chair'

    @classmethod
    def CreateConferenceChair(cls, email, username, password, Name):

        newConfChair = cls(email = email, username=username, password=password, Name = Name)

        newConfChair.save()

        return True
    
    def getConferenceChair(username, password):
        try:
            confChair = ConferenceChair.objects.get(username=username,password=password)

            return confChair
        except (ConferenceChair.DoesNotExist, ObjectDoesNotExist):
            return None
    
    def getAllConferenceChair():
        confChair_list = ConferenceChair.objects.all().values()

        return confChair_list






