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
    status = models.CharField(max_length = 1, default="0") #0:Active 1:Inactive

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
    
    def UpdateRoleByID(id, email, username, password, name, maxPaper, role):
        if(email.replace(" ","")=="" or username.replace(" ","") == "" or password.replace(" ","") == "" or name.replace(" ","") == ""):
            return False

        try:
            admin = SystemAdmin.objects.get(id = id)
            admin.setStatus("1")

            if(role=="Reviewer"):
                reviewer = Reviewer(users_ptr_id = id, name = name, maxPaper = maxPaper)
                reviewer.username = username
                reviewer.password = password
                reviewer.email = email
                reviewer.save()
                
            elif(role=="Author"):
                author = Author(users_ptr_id = id, name = name)
                author.username = username
                author.password = password
                author.email = email
                author.save()

            elif(role=="Conference Chair"):
                conf = ConferenceChair(users_ptr_id = id, name=name)
                conf.username = username
                conf.password = password
                conf.email = email
                conf.save()

            return True

        except (SystemAdmin.DoesNotExist, ObjectDoesNotExist):
            return False

    #Get specific system admin user
    def getSystemAdmin(username, password):
        try:
            systemAdmin = SystemAdmin.objects.get(username=username,password=password,status="0")

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
    
    def getAllActiveSystemAdmin():
        system_list = SystemAdmin.objects.filter(status="0").values()

        return system_list
    
    def setStatus(self, status):
        
        self.status = status
        
        self.save()

        return True

class Author(Users):
    name = models.CharField(max_length = 255)
    status = models.CharField(max_length = 1, default="0") #0:Active 1:Inactive

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

    def UpdateRoleByID(id, email, username, password, name,maxPaper, role):
        if(email.replace(" ","")=="" or username.replace(" ","") == "" or password.replace(" ","") == "" or name.replace(" ","") == ""):
            return False

        try:
            author = Author.objects.get(id=id)
            author.setStatus("1")

            if(role=="Reviewer"):
                reviewer = Reviewer(users_ptr_id = id, name = name, maxPaper = maxPaper)
                reviewer.username = username
                reviewer.password = password
                reviewer.email = email
                reviewer.save()
                
            elif(role=="Conference Chair"):
                conf = ConferenceChair(users_ptr_id = id, name=name)
                conf.username = username
                conf.password = password
                conf.email = email
                conf.save()

            elif(role == "System Admin"):
                admin = SystemAdmin(users_ptr_id=id)
                admin.username = username
                admin.password=password
                admin.email = email
                admin.save()

            return True

        except (Author.DoesNotExist, ObjectDoesNotExist):
            return False

    #Get specific author user
    def getAuthor(username, password):
        try:
            author = Author.objects.get(username=username,password=password,status="0")

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

    def getAllActiveAuthor():
        author_list = Author.objects.filter(status="0").values()

        return author_list
    
    def getAllActiveAuthorWithoutLoggedAuthor(id):
        author_list = Author.getAllActiveAuthor().exclude(id=id)

        return author_list

    def getAuthorEmail(id):
        author_email = Author.objects.get(id=id).email

        return author_email

    def setStatus(self, status):
        
        self.status = status
        
        self.save()

        return True

class Reviewer(Users):
    maxPaper = models.IntegerField(default = 0)
    name = models.CharField(max_length = 255)
    status = models.CharField(max_length = 1, default="0") #0:Active 1:Inactive

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
            reviewer.maxPaper = int(maxPaper)

            reviewer.save()

            return True
        except (Reviewer.DoesNotExist, ObjectDoesNotExist):
            return False

    def UpdateRoleByID(id, email, username, password, name,maxPaper, role):
        if(email.replace(" ","")=="" or username.replace(" ","") == "" or password.replace(" ","") == "" or name.replace(" ","") == ""):
            return False

        try:
            reviewer = Reviewer.objects.get(id=id)
            reviewer.setStatus("1")

            if(role=="Author"):
                author = Author(users_ptr_id = id, name = name)
                author.username = username
                author.password = password
                author.email = email
                author.save()

            elif(role=="Conference Chair"):
                conf = ConferenceChair(users_ptr_id = id, name=name)
                conf.username = username
                conf.password = password
                conf.email = email
                conf.save()

            elif(role == "System Admin"):
                admin = SystemAdmin(users_ptr_id=id)
                admin.username = username
                admin.password=password
                admin.email = email
                admin.save()

            return True

        except (Reviewer.DoesNotExist, ObjectDoesNotExist):
            return False

    def getReviewer(username, password):
        try:
            reviewer = Reviewer.objects.get(username=username,password=password,status="0")

            return reviewer
        except (Reviewer.DoesNotExist, ObjectDoesNotExist):
            return None

    def getReviewerByID(id):
        try:
            reviewer = Reviewer.objects.get(id=id)

            return reviewer
        except (Reviewer.DoesNotExist, ObjectDoesNotExist):
            return None

    def getMaxPaperByID(id):
        try:
            reviewer = Reviewer.objects.get(id=id)

            return reviewer.maxPaper
        except (Reviewer.DoesNotExist, ObjectDoesNotExist):
            return None
   
    def setMaxPaperByID(id, maxPaper):
        try:
            reviewer = Reviewer.objects.get(id=id)

            reviewer.maxPaper = int(maxPaper)

            reviewer.save()

            return True
        except (Reviewer.DoesNotExist, ObjectDoesNotExist):
            return False
    
    def setStatus(self, status):
        self.status = status
        self.save()
        
        return True

    def getAllReviewer():
        reviewer_list = Reviewer.objects.all().values()

        return reviewer_list
    
    def getAllActiveReviewer():
        reviewer_list = Reviewer.objects.filter(status="0").values()

        return reviewer_list
    
class ConferenceChair(Users):
    name = models.CharField(max_length = 255)
    status = models.CharField(max_length = 1, default="0") #0:Active 1:Inactive

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

    def UpdateRoleByID(id, email, username, password, name, maxPaper, role):
        if(email.replace(" ","")=="" or username.replace(" ","") == "" or password.replace(" ","") == "" or name.replace(" ","") == ""):
            return False

        try:
            conference = ConferenceChair.objects.get(id = id)
            conference.setStatus("1")

            if(role=="Reviewer"):
                reviewer = Reviewer(users_ptr_id = id, name = name, maxPaper = maxPaper)
                reviewer.username = username
                reviewer.password = password
                reviewer.email = email
                reviewer.save()
                
            elif(role=="Author"):
                author = Author(users_ptr_id = id, name = name)
                author.username = username
                author.password = password
                author.email = email
                author.save()

            elif(role == "System Admin"):
                admin = SystemAdmin(users_ptr_id=id)
                admin.username = username
                admin.password=password
                admin.email = email
                admin.save()

            return True

        except (ConferenceChair.DoesNotExist, ObjectDoesNotExist):
            return False
    
    def getConferenceChair(username, password):
        try:
            confChair = ConferenceChair.objects.get(username=username,password=password,status="0")

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

    def getAllActiveConferenceChair():
        confChair_list = ConferenceChair.objects.filter(status="0").values()

        return confChair_list

    def setStatus(self, status):
        self.status = status
        self.save()
        
        return True

class Paper(models.Model):
    topic= models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    submitted_date = models.DateTimeField(default = timezone.now)
    fileName = models.CharField(max_length = 255)
    saved_file = models.FileField(upload_to = 'website/files')
    authors = models.ManyToManyField(Author) # multiple authors
    uploaded_by = models.CharField(max_length=255) # author_id
    status = models.CharField(max_length=255, default = "Not Accessed") # not accessed, rejected, accepted

    class Meta:
        db_table = 'paper'

    @classmethod
    def createPaper(cls, topic, description, fileName, saved_file, authors, uploaded_by):
        paper= cls(topic = topic, description = description, fileName = fileName, saved_file = saved_file, uploaded_by = uploaded_by)
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

    def updateStatus(self, status):
        self.status = status
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

    # author controller
    def viewPaper(id):
        paper_list = Paper.objects.all().filter(authors__in=[id])

        return paper_list
    
    def deleteSubmittedPaper(id):
        paper = Paper.getPaper(id)
        paper.delete()

        return True

    def readSubmittedPaper(id):
        paper = Paper.getPaper(id)
        text = paper.saved_file.read().decode("utf-8")

        return text

    def getAllAuthorID(self):
        authors = list(self.authors.values_list('id', flat = True))
        print(authors)
        
        return authors

class Bidded_Paper(models.Model):
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    bid_date = models.DateTimeField(default = timezone.now)
    submission_date = models.DateTimeField(default = None, null=True)
    status = models.CharField(max_length=255, default = "0") #0 = Unassigned, 1 = Assigned, 2 = Review Complete

    class Meta:
        db_table = 'bidded_paper'

    @classmethod
    def createBiddedPaper(cls, reviewer_id, paper, status):

        reviewer = Reviewer.getReviewerByID(reviewer_id)

        bidded_paper = cls(reviewer = reviewer, paper = paper, status = status)

        bidded_paper.save()

        return True
    
    def updateStatus(self, status):
        self.status = status
        self.save()
        
        return True

    def updateSubmission(self, datetime):
        self.submission_date = datetime
        self.save()

        return True

    def getBiddedPaper(id):
        try:
            biddedPaper = Bidded_Paper.objects.get(id = id)

            return biddedPaper
        except (Bidded_Paper.DoesNotExist, ObjectDoesNotExist):
            return None
    
    def getAllBiddedPaper():
        biddedPaper_list = Bidded_Paper.objects.all().values() 
        return biddedPaper_list
        
    def getAllUnassignedPaperByID(id):

        reviewer = Reviewer.getReviewerByID(id)

        bid_list = Bidded_Paper.objects.filter(reviewer = reviewer).filter(status='0').values()

        return bid_list

    def getAllAssignedPaperByID(id):

        reviewer = Reviewer.getReviewerByID(id)

        bid_list = Bidded_Paper.objects.filter(reviewer = reviewer).filter(status='1').values()

        return bid_list

    def getAllReviewedPaperByID(id):

        reviewer = Reviewer.getReviewerByID(id)

        bid_list = Bidded_Paper.objects.filter(reviewer = reviewer).filter(status='2').values()

        return bid_list

    def deleteBiddedPaperByID(id):
        try:
            biddedPaper = Bidded_Paper.objects.get(id=id)
            biddedPaper.delete()

            return True
        except(Bidded_Paper.DoesNotExist, ObjectDoesNotExist):

            return False
    
    def deleteBiddedPape(self):
        self.delete()

        return True
           
class Review(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    title = models.CharField(max_length=255, default="No Title")
    description = models.TextField()

    class Meta:
        db_table = 'review'

    @classmethod
    def createReview(cls, paper, reviewer, rating, title, description):
        review = cls(paper = paper, reviewer = reviewer, rating = int(rating), title = title, description = description)
        review.save()

        return True

    def updateReview(id, rating, title, description):

        review = Review.getReview(id)

        review.rating = int(rating)
        review.title = title
        review.description = description

        review.save()

        return True

    def deleteReview(self):

        self.delete()

        return True

    def getReview(id):
        try:
            review = Review.objects.get(id = id)

            return review
        except (Review.DoesNotExist, ObjectDoesNotExist):
            return None
    def getReviewByPaperAndReviewer(paper_id, reviewer_id):
        try:
            review = Review.objects.get(paper_id = paper_id, reviewer_id = reviewer_id)

            return review
        except (Review.DoesNotExist, ObjectDoesNotExist):
            return None

    
    def getOtherReviews(paper_id, reviewer_id):
        reviews = Review.objects.filter(paper_id=paper_id).exclude(reviewer_id=reviewer_id).values()

        return reviews

    def getAllReviewByPaperID(id):
        return False

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    commenter = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    description = models.TextField()
    sent_date = models.DateTimeField(default = timezone.now)

    class Meta:
        db_table = 'comment'

    @classmethod
    def createComment(cls, review, commenter, rating, description):
        comment = cls(review = review, commenter = commenter, rating = rating, description = description)
        comment.save()

        return True

    def updateComment(id, rating, description):
        return False

    def deleteComment(id):
        return False

    def getAllCommentByReviewID(id):
        return False
