from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from django.db.models import Q
from django.core.mail import send_mail

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

    def getAuthorName(id):
        author_name = Author.objects.get(id=id).name

        return author_name

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
    
    def updatePaper(id, topic, description, saved_file, authors):

        paper = Paper.getPaper(id)
        author_id = int(paper.uploaded_by)
        
        new_fileLocation = saved_file
        new_fileName = str(new_fileLocation)

        if(new_fileLocation == False):
            new_fileName = paper.fileName
            new_fileLocation = paper.saved_file

        if len(authors) == 0:
            authors = paper.getAllAuthorID() 
        else:
            authors.append(author_id)

        paper.topic = topic
        paper.description = description

        paper.fileName = new_fileName
        paper.saved_file = new_fileLocation
        paper.authors.clear()

        for author_id in authors:
            author = Author.objects.get(id=author_id)
            paper.authors.add(author)

        paper.save()

        return True

    def updateStatusToAccepted(id):
        paper = Paper.getPaper(id)

        paper.status = "Accepted"
        paper.save()

        author_id_list = Paper.getAllAuthorIDByPaperID(id)

        for author_id in author_id_list:
            author_email = Author.getAuthorEmail(author_id)
            content = f'Dear Author ID {author_id}, your paper, {paper.topic} , is accepted. Thank you.'
            
            send_mail('Acceptation of Paper',
            content, 
            'nextlevelt05@gmail.com', 
            [author_email], 
            fail_silently=False)
        
        return True

    def updateStatusToRejected(id):
        paper = Paper.getPaper(id)

        paper.status = "Rejected"
        paper.save()

        author_id_list = Paper.getAllAuthorIDByPaperID(id)

        for author_id in author_id_list:
            author_email = Author.getAuthorEmail(author_id)
            content = f'Dear Author ID {author_id}, your paper, {paper.topic} , is rejected. Thank you.'
            
            send_mail('Rejection of Paper',
            content, 
            'nextlevelt05@gmail.com', 
            [author_email], 
            fail_silently=False)
        
        return True

    def updateStatusToNotAccessed(id):
        paper = Paper.getPaper(id)

        paper.status = "Not Accessed"
        paper.save()

        author_id_list = Paper.getAllAuthorIDByPaperID(id)

        for author_id in author_id_list:
            author_email = Author.getAuthorEmail(author_id)
            content = f'Dear Author ID {author_id}, the decision of your paper, {paper.topic} , has been canceled. Thank you.'
            
            send_mail('Cancellation of decision made',
            content, 
            'nextlevelt05@gmail.com', 
            [author_email], 
            fail_silently=False)
        
        return True

    def getPaper(id):
        try:
            paper = Paper.objects.get(id = id)

            return paper
        except (Paper.DoesNotExist, ObjectDoesNotExist):
            return None

    def getPaperContent(id):
        text = Paper.readSubmittedPaper(id)

        paper = Paper.getPaper(id)

        context = {'paper':paper, 'content': text}

        return context
        
        
    def getAllPaper():
        paper_list = Paper.objects.all().values()

        return paper_list

    def getAllUnbiddedPaper(reviewer_id):

        reviewer = Reviewer.getReviewerByID(reviewer_id)

        bid_list = Bidded_Paper.objects.filter(reviewer = reviewer).values_list('paper_id', flat=True)

        paper_list = Paper.objects.exclude(id__in=list(bid_list))

        return paper_list

    # author controller
    def getAllPaperByAuthorID(id):
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
        authors=list(self.authors.values_list('id', flat=True))
        print(authors)
        
        return authors
    
    def getAllAuthorIDByPaperID(id):
        paper = Paper.getPaper(id)

        authors = list(paper.authors.values_list('id', flat = True))
        print(authors)
        
        return authors

    def getText(self):
        text = self.saved_file.read().decode("utf-8")

        return text

    def getAllUnAccessedPaper():
        paper_list = Paper.objects.filter(status="Not Accessed").all()
        
        return paper_list
    
    def getAllAcceptedRejectedPaper():
        paper_list = Paper.objects.filter(~Q(status="Not Accessed"))
        
        return paper_list
    
    def getPaperStatus(self):
        return self.status

class Bidded_Paper(models.Model):
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    bid_date = models.DateTimeField(default = timezone.now)
    submission_date = models.DateTimeField(default = None, null=True)
    status = models.CharField(max_length=255, default = "0") #0 = Unassigned, 1 = Assigned, 2 = Review Complete

    class Meta:
        db_table = 'bidded_paper'

    @classmethod
    def createBiddedPaper(cls, reviewer_id, paper_id, status):

        reviewer = Reviewer.getReviewerByID(reviewer_id)

        paper = Paper.getPaper(paper_id)

        bidded_paper = cls(reviewer = reviewer, paper = paper, status = status)

        bidded_paper.save()

        return True
    
    def updateStatus(self, status):
        self.status = status
        self.save()
        
        return True

    def updateStatusToAllocated(paper_id, reviewer_id):
        # check if number of paper < max paper
        numOfPaperAssigned = Bidded_Paper.getNumberOfAssignedPaperByReviewerID(reviewer_id)
        maxPaper = Reviewer.getMaxPaperByID(reviewer_id)

        if numOfPaperAssigned < maxPaper:
            bidded_papers = Bidded_Paper.getPaperByPaperIDAndReviewerID(paper_id, reviewer_id)
            for bidded_paper in bidded_papers:
                success = bidded_paper.updateStatus(1)
                if(success):
                    return "Success"
                else:
                    return "Error 1"
        else:
            return "Error 2"

    def updateStatusToUnallocate(paper_id, reviewer_id):

        bidded_paper = Bidded_Paper.getAssignedPaperByPaperIDAndReviewerID(paper_id, reviewer_id)
        success = bidded_paper.updateStatus(0)

        return success

    def updateSubmission(self, datetime):
        self.submission_date = datetime
        self.save()

        return True

    def AutoAllocate():
        bidded_paper = Bidded_Paper.getAllUnassignedBiddedPaper()
        for paper in bidded_paper:
            bid_paper = Bidded_Paper.getBiddedPaper(paper['id'])
            reviewer_id = paper['reviewer_id']
            paper_id = paper['paper_id']
            maxPaper = Reviewer.getMaxPaperByID(reviewer_id)
            numOfPaperAssigned = Bidded_Paper.getAllAssignedPaperByID(reviewer_id).count()

            if numOfPaperAssigned < maxPaper:
                success = bid_paper.updateStatus(1)

        return success

    def getBiddedPaper(id):
        try:
            biddedPaper = Bidded_Paper.objects.get(id = id)

            return biddedPaper
        except (Bidded_Paper.DoesNotExist, ObjectDoesNotExist):
            return None
    
    def getAllBiddedPaper():
        biddedPaper_list = Bidded_Paper.objects.all().values() 
        return biddedPaper_list

    def getAllUnassignedBiddedPaper():
        biddedPaper_list = Bidded_Paper.objects.filter(status = 0).values()

        return biddedPaper_list
        
    def getAllUnassignedPaperByID(id):

        reviewer = Reviewer.getReviewerByID(id)

        bid_list = Bidded_Paper.objects.filter(reviewer = reviewer).filter(status='0').values()

        return bid_list

    def getAllAssignedPaperByID(id):

        reviewer = Reviewer.getReviewerByID(id)

        bid_list = Bidded_Paper.objects.filter(reviewer = reviewer).filter(status='1').values()

        return bid_list
    
    def getAssignedPaperByPaperIDAndReviewerID(paper_id, reviewer_id):
        bid_list = Bidded_Paper.objects.filter(status=1).filter(paper_id=paper_id).filter(reviewer_id=reviewer_id)

        return bid_list[0]

    def getAllUnassignedPaperID():
        paper_id_list = Bidded_Paper.objects.all().filter(status=0).values('paper_id').distinct()

        return paper_id_list

    def getAllAssignedPaperID():
            paper_id_list = Bidded_Paper.objects.all().filter(status=1).values('paper_id').distinct()

            return paper_id_list

    def getAllUnassignedReviewerID(paper_id):
        reviewer_id_list = Bidded_Paper.objects.filter(status=0).filter(paper_id=paper_id['paper_id']).values('reviewer_id').distinct()

        return reviewer_id_list
    
    def getAllAssignedReviewerID(paper_id):
        reviewer_id_list = Bidded_Paper.objects.filter(status=1).filter(paper_id=paper_id).values('reviewer_id').distinct()

        return reviewer_id_list
    
    def getNumberOfAssignedPaperByReviewerID(reviewer_id):
        numberOfAssignedPaperByreviewerID = Bidded_Paper.objects.filter(status=1).filter(reviewer_id = reviewer_id).count()
        
        return numberOfAssignedPaperByreviewerID

    def getPaperByPaperIDAndReviewerID(paper_id, reviewer_id):
        bid_list = Bidded_Paper.objects.filter(paper_id=paper_id).filter(reviewer_id=reviewer_id)

        return bid_list
    
    def getAllReviewerIDunassignedPaper(paper_id):
        bid_list = Bidded_Paper.objects.filter(status=0).filter(paper_id=paper_id).values_list('reviewer_id').distinct()

        return bid_list

    def getAllReviewedPaperByID(id):

        reviewer = Reviewer.getReviewerByID(id)

        bid_list = Bidded_Paper.objects.filter(reviewer = reviewer).filter(status='2').values()

        return bid_list

    def GetAllUnassignedPapers():
        # need to be allocated table
        unassigned_paper_id_list = Bidded_Paper.getAllUnassignedPaperID()

        for paper_id in unassigned_paper_id_list:
            reviewer = []
            unassigned_reviewer_id_list = Bidded_Paper.getAllUnassignedReviewerID(paper_id)
            for reviewer_id in unassigned_reviewer_id_list:
                reviewer.append(reviewer_id['reviewer_id'])
            paper_id['reviewer'] = reviewer

        return unassigned_paper_id_list

    def getAllAssignedPapers():
        assigned_paper_id_list = Bidded_Paper.getAllAssignedPaperID()

        for paper_id in assigned_paper_id_list:
            reviewer = []
            assigned_reviewer_id_list = Bidded_Paper.getAllAssignedReviewerID(paper_id['paper_id'])
            for reviewer_id in assigned_reviewer_id_list:
                reviewer.append(reviewer_id['reviewer_id'])
            paper_id['reviewer'] = reviewer

        return assigned_paper_id_list

    def getAllAllocatePaperDetails(id):
        reviewer_id_list = Bidded_Paper.getAllReviewerIDunassignedPaper(id)

        paper = Paper.getPaper(id=id)
        context = {'paper': paper, 'reviewer_id_list': reviewer_id_list}

        return context

    def getAllAssignedAndReviewedPapers(reviewer_id):
        
        assigned_list = Bidded_Paper.getAllAssignedPaperByID(reviewer_id)

        completed_list = Bidded_Paper.getAllReviewedPaperByID(reviewer_id)

        context = {'assigned_list':assigned_list,'completed_list':completed_list}

        return context


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
    def createReview(cls, bid_id, reviewer_id, rating, title, description):

        bidPaper = Bidded_Paper.getBiddedPaper(bid_id)

        paper = Paper.getPaper(bidPaper.paper_id)

        reviewer = Reviewer.getReviewerByID(reviewer_id)

        review = cls(paper = paper, reviewer = reviewer, rating = int(rating), title = title, description = description)
        review.save()

        bidPaper.updateStatus("2")
        bidPaper.updateSubmission(timezone.now())

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

    def getReviewPageDetails(reviewer_id, id):
        reviewer = Reviewer.getReviewerByID(reviewer_id)

        bidPaper = Bidded_Paper.getBiddedPaper(id)

        paper = Paper.getPaper(bidPaper.paper_id)

        review = Review.getReviewByPaperAndReviewer(bidPaper.paper_id, reviewer_id)

        text = paper.getText()

        context = {'paper':paper, 'bid_id':id, 'review':review, 'content': text , 'reviewer':reviewer}

        return context

    def getReviewAndPaperInfo(id):
        try:
            review = Review.getReview(id)
            paper = Paper.getPaper(review.paper_id)
    
            text = paper.getText()

            context = {'review': review, 'paper' : paper, 'content': text}
            
            return context
        except (Review.DoesNotExist, ObjectDoesNotExist):
            return None
    
    def getAllReviewDetailsByPaperID(id):
        reviews = Review.getAllReviewByPaperID(id)

        paper = Paper.getPaper(id)
        text = Paper.readSubmittedPaper(id)

        context = {'reviews' : reviews, 'paper': paper, 'content':text}

        return context

    def getReviewByPaperAndReviewer(bid_id, reviewer_id):

        bidPaper = Bidded_Paper.getBiddedPaper(bid_id)

        try:
            review = Review.objects.get(paper_id = bidPaper.paper_id, reviewer_id = reviewer_id)

            return review
        except (Review.DoesNotExist, ObjectDoesNotExist):
            return None

    
    def getOtherReviews(bid_id, reviewer_id):

        bidPaper = Bidded_Paper.getBiddedPaper(bid_id)
        
        reviews = Review.objects.filter(paper_id=bidPaper.paper_id).exclude(reviewer_id=reviewer_id).values()

        #Get Reviewer Name base on reviewer ID
        for otherReview in reviews:
            print(otherReview)
            reviewer_name = Reviewer.getReviewerByID(otherReview.get("reviewer_id")).name
            otherReview['reviewerName'] = reviewer_name

        return reviews

    def getAllReviewByPaperID(id):
        paper_list = Review.objects.filter(paper_id = id)
        
        return paper_list

    def getAllReview():
        review_list = Review.objects.all()

        return review_list

    def getAllPaperID():
        paper_list = list(Review.objects.values_list('paper_id', flat=True).distinct())

        return paper_list

    def getAllUnReviewedByAuthorReviewsByAuthorID(author_id):
        review_list = Review.getAllReview()
        final_review_list = []
        
        for review in review_list:
            paper = Paper.getPaper(review.paper_id)
            author_list = paper.getAllAuthorID()
            authorHasNotReviewed = ReviewRating.checkAuthorHasNotReviewed(review.paper_id, review.reviewer_id, author_id)

            if author_id in author_list and authorHasNotReviewed:
                final_review_list.append(review)

        return final_review_list

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    commenter = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    description = models.TextField()
    sent_date = models.DateTimeField(default = timezone.now)

    class Meta:
        db_table = 'comment'

    @classmethod
    def createComment(cls, review_id, commenter, rating, description):

        review = Review.getReview(review_id)

        comment = cls(review = review, commenter = commenter, rating = rating, description = description)
        comment.save()

        return True

    def updateComment(id, rating, description):
        comment = Comment.getCommentByID(id)

        comment.rating = rating
        comment.description = description

        comment.save()

        return True

    def deleteComment(id):
        comment = Comment.getCommentByID(id)

        comment.delete()

        return True

    def getCommentByID(id):
        try:
            comment = Comment.objects.get(id=id)

            return comment

        except (Comment.DoesNotExist, ObjectDoesNotExist):
            return None

    def getAllCommentByReviewID(id):
        comments = Comment.objects.filter(review_id = id).values()

        return comments

class ReviewRating(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # created by
    rating = models.IntegerField(default=0)

    class Meta:
        db_table = 'review_rating'

    @classmethod
    def createReviewRating(cls, review_id, paper_id, reviewer_id, author_id, rating):

        review = Review.getReview(review_id)
        paper = Paper.getPaper(paper_id)
        reviewer = Reviewer.getReviewerByID(reviewer_id)
        author = Author.getAuthorByID(author_id)

        reviewRating = cls(review = review, paper = paper, reviewer = reviewer, author = author, rating = int(rating))
        reviewRating.save()

        return True        

    def getAllReviewRating():
        reviewRating_list = ReviewRating.objects.all()

        return reviewRating_list
    
    def getReviewRatingByID(id):
        reviewRating = ReviewRating.objects.get(id=id)
        return reviewRating

    def getAllReviewRatingByAuthorID(author_id):
        reviewRating_list = ReviewRating.getAllReviewRating()
        finalReviewRating_list = []

        for reviewRating in reviewRating_list:
            paper = Paper.getPaper(reviewRating.paper_id)
            author_list = paper.getAllAuthorID()
            if author_id in author_list:
                finalReviewRating_list.append(reviewRating)

        return finalReviewRating_list

    def deleteReviewRating(id):
        reviewRating = ReviewRating.getReviewRatingByID(id)
        reviewRating.delete()

        return True

    def checkAuthorHasNotReviewed(paper_id, reviewer_id, author_id):
        numberOfReview = ReviewRating.objects.filter(paper_id = paper_id).filter(reviewer_id = reviewer_id).filter(author_id = author_id).count()

        if numberOfReview == 0:
            authorHasNotReviewed = True
        else:
            authorHasNotReviewed = False
        
        return authorHasNotReviewed
