from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

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

    def UpdateSysAdminByID(id, email, username, password):

        if(email.replace(" ","")=="" or username.replace(" ","") == "" or password.replace(" ","") == ""):
            return False

        try:
            admin = SystemAdmin.objects.get(id = id)
            admin.email = email
            admin.username = username
            admin.password = password

            admin.save()

            return True
        except (SystemAdmin.DoesNotExist, ObjectDoesNotExist):
            return False

    #Get specific system admin user
    def getSystemAdmin(username, password):
        try:
            systemAdmin = SystemAdmin.objects.get(username=username,password=password)

            return systemAdmin
        except (SystemAdmin.DoesNotExist, ObjectDoesNotExist):
            return None

    def getSystemAdminByID(id):
        try:
            systemAdmin = SystemAdmin.objects.get(id=id)

            return systemAdmin
        except (SystemAdmin.DoesNotExist, ObjectDoesNotExist):
            return None

    #Get All System Admins
    def getAllSystemAdmin():
        system_list = SystemAdmin.objects.all().values()

        return system_list

class Author(Users):
    name = models.CharField(max_length = 255)

    class Meta(User.Meta):
        db_table = 'author'

    @classmethod
    def createAuthor(cls, email, username, password, name):

        if(email.replace(" ","")=="" or username.replace(" ","") == "" or password.replace(" ","") == "" or name.replace(" ","") == ""):
            return False

        newAuthor = cls(email = email, username=username, password=password, name = name)

        newAuthor.save()

        return True

    def UpdateAuthorByID(id, email, username, password, name):

        if(email.replace(" ","")=="" or username.replace(" ","") == "" or password.replace(" ","") == "" or name.replace(" ","") == ""):
            return False

        try:
            author = Author.objects.get(id = id)
            author.email = email
            author.username = username
            author.password = password
            author.name = name

            author.save()

            return True
        except (Author.DoesNotExist, ObjectDoesNotExist):
            return False

    #Get specific author user
    def getAuthor(username, password):
        try:
            author = Author.objects.get(username=username,password=password)

            return author
        except (Author.DoesNotExist, ObjectDoesNotExist):
            return None

    def getAuthorByID(id):
        try:
            author = Author.objects.get(id=id)

            return author
        except (Reviewer.DoesNotExist, ObjectDoesNotExist):
            return None
    
    def getAllAuthor():
        author_list = Author.objects.all().values()

        return author_list

class Reviewer(Users):
    maxPaper = models.IntegerField(default = 0)
    name = models.CharField(max_length = 255)

    class Meta(User.Meta):
        db_table = 'reviewer'

    @classmethod
    def createReviewer(cls, email, username, password, name, maxPaper):

        if(email.replace(" ","")=="" or username.replace(" ","") == "" or password.replace(" ","") == "" or name.replace(" ","") == ""or maxPaper.replace(" ","") == ""):
            return False

        newReviewer = cls(email = email, username=username, password=password, name = name, maxPaper = int(maxPaper))

        newReviewer.save()

        return True
    
    def UpdateReviewerByID(id, email, username, password, name, maxPaper):

        if(email.replace(" ","")=="" or username.replace(" ","") == "" or password.replace(" ","") == "" or name.replace(" ","") == ""or maxPaper.replace(" ","") == ""):
            return False

        try:
            reviewer = Reviewer.objects.get(id = id)
            reviewer.email = email
            reviewer.username = username
            reviewer.password = password
            reviewer.name = name
            reviewer.maxPaper = maxPaper

            reviewer.save()

            return True
        except (Reviewer.DoesNotExist, ObjectDoesNotExist):
            return False

    def getReviewer(username, password):
        try:
            reviewer = Reviewer.objects.get(username=username,password=password)

            return reviewer
        except (Reviewer.DoesNotExist, ObjectDoesNotExist):
            return None

    def getReviewerByID(id):
        try:
            reviewer = Reviewer.objects.get(id=id)

            return reviewer
        except (Reviewer.DoesNotExist, ObjectDoesNotExist):
            return None
    
    def getAllReviewer():
        reviewer_list = Reviewer.objects.all().values()

        return reviewer_list
    
class ConferenceChair(Users):
    name = models.CharField(max_length = 255)

    class Meta(User.Meta):
        db_table = 'conference_chair'

    @classmethod
    def CreateConferenceChair(cls, email, username, password, name):

        if(email.replace(" ","")=="" or username.replace(" ","") == "" or password.replace(" ","") == "" or name.replace(" ","") == ""):
            return False

        newConfChair = cls(email = email, username=username, password=password, name = name)

        newConfChair.save()

        return True

    def UpdateConferenceChairByID(id, email, username, password, name):

        if(email.replace(" ","")=="" or username.replace(" ","") == "" or password.replace(" ","") == "" or name.replace(" ","") == ""):
            return False

        try:
            conference = ConferenceChair.objects.get(id = id)
            conference.email = email
            conference.username = username
            conference.password = password
            conference.name = name

            conference.save()

            return True
        except (ConferenceChair.DoesNotExist, ObjectDoesNotExist):
            return False
    
    def getConferenceChair(username, password):
        try:
            confChair = ConferenceChair.objects.get(username=username,password=password)

            return confChair
        except (ConferenceChair.DoesNotExist, ObjectDoesNotExist):
            return None
    
    def getConferenceChairByID(id):
        try:
            confChair = ConferenceChair.objects.get(id = id)

            return confChair
        except (ConferenceChair.DoesNotExist, ObjectDoesNotExist):
            return None
    
    def getAllConferenceChair():
        confChair_list = ConferenceChair.objects.all().values()

        return confChair_list

class Paper(models.Model):
    topic= models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    submitted_date = models.DateTimeField(default = timezone.now)
    fileName = models.CharField(max_length = 255)
    saved_file = models.FileField(upload_to = 'website/files')
    authors = models.ManyToManyField(Author)

    @classmethod
    def createPaper(cls, topic, description, fileName, saved_file, authors):
        paper= cls(topic = topic, description = description, fileName = fileName, saved_file = saved_file)
        paper.save()

        for author_id in authors:
            author = Author.objects.get(id=author_id)
            paper.authors.add(author)

        return True
    
    def updatePaper(self, topic, description, fileName, saved_file, authors):
        self.topic = topic
        self.description = description
        self.fileName = fileName
        self.saved_file = saved_file
        self.authors.clear()

        for author_id in authors:
            author = Author.objects.get(id=author_id)
            self.authors.add(author)

        self.save()

        return True

    def getPaper(id):
        try:
            paper = Paper.objects.get(id = id)

            return paper
        except (Paper.DoesNotExist, ObjectDoesNotExist):
            return None
        
        
    def getAllPaper():
        paper_list = Paper.objects.all().values()

        return paper_list

    def getAllUnbiddedPaper(reviewer_id):

        reviewer = Reviewer.getReviewerByID(reviewer_id)

        bid_list = Bidded_Paper.objects.filter(reviewer = reviewer).values_list('paper_id', flat=True)

        paper_list = Paper.objects.exclude(id__in=list(bid_list))

        return paper_list

class Bidded_Paper(models.Model):
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    bid_date = models.DateTimeField(default = timezone.now)
    submission_date = models.DateTimeField(default = None, null=True)
    status = models.CharField(max_length=255, default = "0")

    @classmethod
    def createBiddedPaper(cls, reviewer_id, paper, status):

        reviewer = Reviewer.getReviewerByID(reviewer_id)

        bidded_paper = cls(reviewer = reviewer, paper = paper, status = status)

        bidded_paper.save()

        return True
    
    def getAllBiddedPaperByID(id):

        reviewer = Reviewer.getReviewerByID(id)

        bid_list = Bidded_Paper.objects.filter(reviewer = reviewer).values()

        return bid_list


class Review(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    description = models.TextField()

    @classmethod
    def createReview(cls, paper, reviewer_name, rating, description):
        review = cls(paper = paper, reviewer_name = reviewer_name, rating = rating, description = description)
        review.save()

        return True
