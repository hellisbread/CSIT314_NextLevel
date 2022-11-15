from django.test import TestCase, Client
from django.urls import reverse

from .models import User, Reviewer, ConferenceChair, Author, SystemAdmin

import json

class Sprint1_TestCases(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.checklogin_url = reverse('login')
        self.admin_url = reverse('systemAdminPage')
        self.createUser_url = reverse('register')
    
    #Test if View/Boundary is correct
    def testView(self):

        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    #Test if system admin will be logged in to correct url upon POST
    def test_login_admin_POST(self):
        #Create System Admin Object as Sample Login
        self.admin1 = SystemAdmin.objects.create(
            email= "sys123@gmail.com",
            username="sys123",
            password="sys123"
        )

        #Attempt to Login
        response = self.client.post(self.checklogin_url, {
            'roleList' : 'System Admin',
            'username':'sys123',
            'password': 'sys123'
        })

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/admin/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

    #Test if View/Boundary is correct
    def test_adminPage_view(self):
        #Sample Session via Logging in with sys123
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        response = self.client.get(self.admin_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/systemAdmin.html")

    #Test Retrieve Functions to display all users same in context
    def test_adminPage_get(self):
        #Sample Data
        self.author1 = Author.objects.create(
            email="a123@gmail.com",
            username="a123",
            password="a123",
            name="Author 123"
        )

        self.reviewer1 = Reviewer.objects.create(
            email="r123@gmail.com",
            username='r123',
            password='r123',
            name = 'Reviewer 123',
            maxPaper = 123
        )

        self.conf1 = ConferenceChair.objects.create(
            email = "c123@gmail.com",
            username="c123",
            password="c123",
            name="Conference 123"
        )

        self.admin1 = SystemAdmin.objects.create(
            email= "sys123@gmail.com",
            username="sys123",
            password="sys123"
        )

        #Sample Session via Logging in with sys123
        session = self.client.session
        session['SysAdminLogged'] = self.admin1.id
        session.save()

        response = self.client.get(self.admin_url)

        author_queryset = Author.getAllActiveAuthor()
        reviewer_queryset = Reviewer.getAllActiveReviewer()
        conf_queryset = ConferenceChair.getAllActiveConferenceChair()
        admin_queryset = SystemAdmin.getAllActiveSystemAdmin()

        self.assertQuerysetEqual(response.context['authors'], author_queryset)
        self.assertQuerysetEqual(response.context['confchairs'], conf_queryset)
        self.assertQuerysetEqual(response.context['reviewers'], reviewer_queryset)
        self.assertQuerysetEqual(response.context['sysadmins'], admin_queryset)

    #Test if View/Boundary is correct
    def test_createUser_view(self):
        #Sample Session via Logging in with sys123
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        response = self.client.get(self.createUser_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/create_user.html")

    #Test create Reviewer Works
    def test_createReviewer_POST(self):
        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        response = self.client.post(self.createUser_url, {
            'roleList':'Reviewer',
            'email' : "r123@gmail.com",
            'username':'r123',
            'password':'r123',
            'fullname' : 'Reviewer 123',
            'maxpaper' : 123
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Reviewer.objects.first().email, 'r123@gmail.com') #Check Inheritance
        self.assertEquals(Reviewer.objects.first().name, 'Reviewer 123') #Check Child

    #Test create Author Works
    def test_createAuthor_POST(self):
        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        response = self.client.post(self.createUser_url, {
            'roleList':'Author',
            'email' : "a123@gmail.com",
            'username':'a123',
            'password':'a123',
            'fullname' : 'Author 123'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Author.objects.first().email, 'a123@gmail.com') #Check Inheritance
        self.assertEquals(Author.objects.first().name, 'Author 123') #Check Child

    #Test create Conference Chair Works
    def test_createConference_POST(self):
        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        response = self.client.post(self.createUser_url, {
            'roleList':'Conference Chair',
            'email' : "c123@gmail.com",
            'username':'c123',
            'password':'c123',
            'fullname' : 'Conference 123'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(ConferenceChair.objects.first().email, 'c123@gmail.com') #Check Inheritance
        self.assertEquals(ConferenceChair.objects.first().name, 'Conference 123') #Check Child

    #Test create Admin Works
    def test_createAdmin_POST(self):
        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        response = self.client.post(self.createUser_url, {
            'roleList':'System Admin',
            'email' : "sys123@gmail.com",
            'username':'sys123',
            'password':'sys123'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(SystemAdmin.objects.first().email, 'sys123@gmail.com') #Check Inheritance
        self.assertEquals(SystemAdmin.objects.first().id, 1) #Check Child

    #Test if reviewer will be logged in to correct url upon POST
    def test_login_reviewer_POST(self):
        #Create Reviewer Object as Sample Login
        self.reviewer1 = Reviewer.objects.create(
            email="r123@gmail.com",
            username='r123',
            password='r123',
            name = 'Reviewer 123',
            maxPaper = 123
        )

        #Attempting to Login
        response = self.client.post(self.checklogin_url, {
            'roleList' : 'Reviewer',
            'username':'r123',
            'password': 'r123'
        })

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/reviewer/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

    #Test if author will be logged in to correct url upon POST
    def test_login_author_POST(self):
        #Create Author Object as Sample Login
        self.author1 = Author.objects.create(
            email="a123@gmail.com",
            username="a123",
            password="a123",
            name="Author 123"
        )

        #Attempt to Login
        response = self.client.post(self.checklogin_url, {
            'roleList' : 'Author',
            'username':'a123',
            'password': 'a123'
        })

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/author/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

    #Test if conference chair will be logged in to correct url upon POST
    def test_login_conf_POST(self):
        #Create Conference Chair Object as Sample Login
        self.conf1 = ConferenceChair.objects.create(
            email = "c123@gmail.com",
            username="c123",
            password="c123",
            name="Conference 123"
        )

        #Attempt to Login
        response = self.client.post(self.checklogin_url, {
            'roleList' : 'Conference Chair',
            'username':'c123',
            'password': 'c123'
        })

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/conferenceChair/allocationPaper/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

    #Test if View/Boundary is correct
    def test_updateAdmin_view(self):
        #Sample Admin Object
        self.admin1 = SystemAdmin.objects.create(
            email= "sys123@gmail.com",
            username="sys123",
            password="sys123"
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        response = self.client.get(reverse('update_admin', args=[self.admin1.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/update_admin.html")

    #Test update Admin
    def test_updateAdmin_info_POST(self):
        #Sample Admin Object
        self.admin1 = SystemAdmin.objects.create(
            email= "sys123@gmail.com",
            username="sys123",
            password="sys123"
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        response = self.client.post(reverse('update_admin', args=[self.admin1.id]), {
            'roleList' :'System Admin',
            'email' : 'sys124@gmail.com',
            'username': 'sys124',
            'password': 'sys124'
        })

        self.assertEquals(response.status_code, 302)
        #Check if updated
        self.assertEquals(SystemAdmin.objects.first().email, "sys124@gmail.com") 
        self.assertEquals(SystemAdmin.objects.first().username, "sys124") 
        self.assertEquals(SystemAdmin.objects.first().password, "sys124") 

    #Test Role Changes Admin to Others
    def test_updateAdminRole_to_Reviewer_POST(self):
        #Sample Admin Object
        self.admin1 = SystemAdmin.objects.create(
            email= "sys123@gmail.com",
            username="sys123",
            password="sys123"
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        #Update to Reviewer
        response = self.client.post(reverse('update_admin', args=[self.admin1.id]), {
            'roleList' :'Reviewer',
            'email' : 'r124@gmail.com',
            'username': 'r124',
            'password': 'r124',
            'fullname': 'Reviewer 124',
            'maxPaper': 124
        })

        self.assertEquals(response.status_code, 302)
        #Check if updated
        self.assertNotEquals(SystemAdmin.objects.first().email, "sys123@gmail.com") 
        self.assertNotEquals(SystemAdmin.objects.first().username, "sys123") 
        self.assertNotEquals(SystemAdmin.objects.first().password, "sys123") 

        self.assertEquals(Reviewer.objects.first().email,"r124@gmail.com")
        self.assertEquals(Reviewer.objects.first().username,"r124")
        self.assertEquals(Reviewer.objects.first().password,"r124")
        self.assertEquals(Reviewer.objects.first().name,"Reviewer 124")
        self.assertEquals(Reviewer.objects.first().maxPaper, 124)

    def test_updateAdminRole_to_Conference_POST(self):
        #Sample Admin Object
        self.admin1 = SystemAdmin.objects.create(
            email= "sys123@gmail.com",
            username="sys123",
            password="sys123"
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        #Update to Reviewer
        response = self.client.post(reverse('update_admin', args=[self.admin1.id]), {
            'roleList' :'Conference Chair',
            'email' : 'c124@gmail.com',
            'username': 'c124',
            'password': 'c124',
            'fullname': 'Conference 124',
            'maxPaper': 0
        })

        self.assertEquals(response.status_code, 302)
        #Check if updated
        self.assertNotEquals(SystemAdmin.objects.first().email, "sys123@gmail.com") 
        self.assertNotEquals(SystemAdmin.objects.first().username, "sys123") 
        self.assertNotEquals(SystemAdmin.objects.first().password, "sys123") 

        self.assertEquals(ConferenceChair.objects.first().email,"c124@gmail.com")
        self.assertEquals(ConferenceChair.objects.first().username,"c124")
        self.assertEquals(ConferenceChair.objects.first().password,"c124")
        self.assertEquals(ConferenceChair.objects.first().name,"Conference 124")

    def test_updateAdminRole_to_Author_POST(self):
        #Sample Admin Object
        self.admin1 = SystemAdmin.objects.create(
            email= "sys123@gmail.com",
            username="sys123",
            password="sys123"
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        #Update to Reviewer
        response = self.client.post(reverse('update_admin', args=[self.admin1.id]), {
            'roleList' :'Author',
            'email' : 'a124@gmail.com',
            'username': 'a124',
            'password': 'a124',
            'fullname': 'Author 124',
            'maxPaper': 0
        })

        self.assertEquals(response.status_code, 302)
        #Check if updated
        self.assertNotEquals(SystemAdmin.objects.first().email, "sys123@gmail.com") 
        self.assertNotEquals(SystemAdmin.objects.first().username, "sys123") 
        self.assertNotEquals(SystemAdmin.objects.first().password, "sys123") 

        self.assertEquals(Author.objects.first().email,"a124@gmail.com")
        self.assertEquals(Author.objects.first().username,"a124")
        self.assertEquals(Author.objects.first().password,"a124")
        self.assertEquals(Author.objects.first().name,"Author 124")

    #Test update Author
    def test_updateAuthor_info_POST(self):
        #Sample Author Object
        self.author1 = Author.objects.create(
            email= "a123@gmail.com",
            username="a123",
            password="a123",
            name= "Author 123"
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        response = self.client.post(reverse('update_author', args=[self.author1.id]), {
            'roleList' :'Author',
            'email' : 'a124@gmail.com',
            'username': 'a124',
            'password': 'a124',
            'fullname': 'Author 124'
        })

        self.assertEquals(response.status_code, 302)
        #Check if updated
        self.assertEquals(Author.objects.first().email, "a124@gmail.com") 
        self.assertEquals(Author.objects.first().username, "a124") 
        self.assertEquals(Author.objects.first().password, "a124")
        self.assertEquals(Author.objects.first().name, "Author 124")  

    #Test Role Changes Author to Others
    def test_updateAuthorRole_to_Reviewer_POST(self):
        #Sample Author Object
        self.author1 = Author.objects.create(
            email= "a123@gmail.com",
            username="a123",
            password="a123",
            name= "Author 123"
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        #Update to Reviewer
        response = self.client.post(reverse('update_author', args=[self.author1.id]), {
            'roleList' :'Reviewer',
            'email' : 'r124@gmail.com',
            'username': 'r124',
            'password': 'r124',
            'fullname': 'Reviewer 124',
            'maxPaper': 124
        })

        self.assertEquals(response.status_code, 302)
        #Check if updated
        self.assertNotEquals(Author.objects.first().email, "a123@gmail.com") 
        self.assertNotEquals(Author.objects.first().username, "a123") 
        self.assertNotEquals(Author.objects.first().password, "a123")  

        self.assertEquals(Reviewer.objects.first().email,"r124@gmail.com")
        self.assertEquals(Reviewer.objects.first().username,"r124")
        self.assertEquals(Reviewer.objects.first().password,"r124")
        self.assertEquals(Reviewer.objects.first().name,"Reviewer 124")
        self.assertEquals(Reviewer.objects.first().maxPaper, 124)

    def test_updateAuthorRole_to_Conference_POST(self):
        #Sample Author Object
        self.author1 = Author.objects.create(
            email= "a123@gmail.com",
            username="a123",
            password="a123",
            name= "Author 123"
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        #Update to Reviewer
        response = self.client.post(reverse('update_author', args=[self.author1.id]), {
            'roleList' :'Conference Chair',
            'email' : 'c124@gmail.com',
            'username': 'c124',
            'password': 'c124',
            'fullname': 'Conference 124',
            'maxPaper': 0
        })

        self.assertEquals(response.status_code, 302)
        #Check if updated
        self.assertNotEquals(Author.objects.first().email, "a123@gmail.com") 
        self.assertNotEquals(Author.objects.first().username, "a123") 
        self.assertNotEquals(Author.objects.first().password, "a123") 

        self.assertEquals(ConferenceChair.objects.first().email,"c124@gmail.com")
        self.assertEquals(ConferenceChair.objects.first().username,"c124")
        self.assertEquals(ConferenceChair.objects.first().password,"c124")
        self.assertEquals(ConferenceChair.objects.first().name,"Conference 124")

    def test_updateAuthorRole_to_Admin_POST(self):
        #Sample Author Object
        self.author1 = Author.objects.create(
            email= "a123@gmail.com",
            username="a123",
            password="a123",
            name= "Author 123"
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        #Update to Admin
        response = self.client.post(reverse('update_author', args=[self.author1.id]), {
            'roleList' :'System Admin',
            'email' : 'sys124@gmail.com',
            'username': 'sys124',
            'password': 'sys124',
            'fullname': '-',
            'maxPaper': 0
        })

        self.assertEquals(response.status_code, 302)
        #Check if updated
        self.assertNotEquals(Author.objects.first().email, "a123@gmail.com") 
        self.assertNotEquals(Author.objects.first().username, "a123") 
        self.assertNotEquals(Author.objects.first().password, "a123")  

        self.assertEquals(SystemAdmin.objects.first().email,"sys124@gmail.com")
        self.assertEquals(SystemAdmin.objects.first().username,"sys124")
        self.assertEquals(SystemAdmin.objects.first().password,"sys124")

    #Test update Reviewer
    def test_updateReviewer_info_POST(self):
        #Sample Reviewer Object
        self.reviewer1 = Reviewer.objects.create(
            email= "r123@gmail.com",
            username="r123",
            password="r123",
            name= "Reviewer 123",
            maxPaper = 123
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        response = self.client.post(reverse('update_reviewer', args=[self.reviewer1.id]), {
            'roleList' :'Reviewer',
            'email' : 'r124@gmail.com',
            'username': 'r124',
            'password': 'r124',
            'fullname': 'Reviewer 124',
            'maxPaper' : 124
        })

        self.assertEquals(response.status_code, 302)
        #Check if updated
        self.assertEquals(Reviewer.objects.first().email, "r124@gmail.com") 
        self.assertEquals(Reviewer.objects.first().username, "r124") 
        self.assertEquals(Reviewer.objects.first().password, "r124")
        self.assertEquals(Reviewer.objects.first().name, "Reviewer 124")
        self.assertEquals(Reviewer.objects.first().maxPaper, 124)  

    #Test Role Changes Reviewer to Others
    def test_updateReviewerRole_to_Author_POST(self):
        #Sample Reviewer Object
        self.reviewer1 = Reviewer.objects.create(
            email= "r123@gmail.com",
            username="r123",
            password="r123",
            name= "Reviewer 123",
            maxPaper = 123
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        #Update to Reviewer
        response = self.client.post(reverse('update_reviewer', args=[self.reviewer1.id]), {
            'roleList' :'Author',
            'email' : 'a124@gmail.com',
            'username': 'a124',
            'password': 'a124',
            'fullname': 'Author 124',
            'maxPaper': 0
        })

        self.assertEquals(response.status_code, 302)
        #Check if updated
        self.assertNotEquals(Reviewer.objects.first().email, "r123@gmail.com") 
        self.assertNotEquals(Reviewer.objects.first().username, "r123") 
        self.assertNotEquals(Reviewer.objects.first().password, "r123")  

        self.assertEquals(Author.objects.first().email,"a124@gmail.com")
        self.assertEquals(Author.objects.first().username,"a124")
        self.assertEquals(Author.objects.first().password,"a124")
        self.assertEquals(Author.objects.first().name,"Author 124")

    def test_updateReviewerRole_to_Conference_POST(self):
        #Sample Reviewer Object
        self.reviewer1 = Reviewer.objects.create(
            email= "r123@gmail.com",
            username="r123",
            password="r123",
            name= "Reviewer 123",
            maxPaper = 123
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        #Update to Reviewer
        response = self.client.post(reverse('update_reviewer', args=[self.reviewer1.id]), {
            'roleList' :'Conference Chair',
            'email' : 'c124@gmail.com',
            'username': 'c124',
            'password': 'c124',
            'fullname': 'Conference 124',
            'maxPaper': 0
        })

        self.assertEquals(response.status_code, 302)
        #Check if updated
        self.assertNotEquals(Reviewer.objects.first().email, "r123@gmail.com") 
        self.assertNotEquals(Reviewer.objects.first().username, "r123") 
        self.assertNotEquals(Reviewer.objects.first().password, "r123")  

        self.assertEquals(ConferenceChair.objects.first().email,"c124@gmail.com")
        self.assertEquals(ConferenceChair.objects.first().username,"c124")
        self.assertEquals(ConferenceChair.objects.first().password,"c124")
        self.assertEquals(ConferenceChair.objects.first().name,"Conference 124")

    def test_updateReviewerRole_to_Admin_POST(self):
        #Sample Reviewer Object
        self.reviewer1 = Reviewer.objects.create(
            email= "r123@gmail.com",
            username="r123",
            password="r123",
            name= "Reviewer 123",
            maxPaper = 123
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        #Update to Admin
        response = self.client.post(reverse('update_reviewer', args=[self.reviewer1.id]), {
            'roleList' :'System Admin',
            'email' : 'sys124@gmail.com',
            'username': 'sys124',
            'password': 'sys124',
            'fullname': '-',
            'maxPaper': 0
        })

        self.assertEquals(response.status_code, 302)
        #Check if updated
        self.assertNotEquals(Reviewer.objects.first().email, "r123@gmail.com") 
        self.assertNotEquals(Reviewer.objects.first().username, "r123") 
        self.assertNotEquals(Reviewer.objects.first().password, "r123")   

        self.assertEquals(SystemAdmin.objects.first().email,"sys124@gmail.com")
        self.assertEquals(SystemAdmin.objects.first().username,"sys124")
        self.assertEquals(SystemAdmin.objects.first().password,"sys124")
    
    #Test update Conference Chair
    def test_updateConference_info_POST(self):
        #Sample Conference Chair Object
        self.conf1 = ConferenceChair.objects.create(
            email= "c123@gmail.com",
            username="c123",
            password="c123",
            name= "Conference 123"
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        response = self.client.post(reverse('update_conference', args=[self.conf1.id]), {
            'roleList' :'Conference Chair',
            'email' : 'c124@gmail.com',
            'username': 'c124',
            'password': 'c124',
            'fullname': 'Conference 124'
        })

        self.assertEquals(response.status_code, 302)
        #Check if updated
        self.assertEquals(ConferenceChair.objects.first().email, "c124@gmail.com") 
        self.assertEquals(ConferenceChair.objects.first().username, "c124") 
        self.assertEquals(ConferenceChair.objects.first().password, "c124")
        self.assertEquals(ConferenceChair.objects.first().name, "Conference 124")

    #Test Role Changes Conference Chair to Others
    def test_updateConferenceRole_to_Author_POST(self):
        #Sample Conference Chair Object
        self.conf1 = ConferenceChair.objects.create(
            email= "c123@gmail.com",
            username="c123",
            password="c123",
            name= "Conference 123"
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        #Update to Reviewer
        response = self.client.post(reverse('update_conference', args=[self.conf1.id]), {
            'roleList' :'Author',
            'email' : 'a124@gmail.com',
            'username': 'a124',
            'password': 'a124',
            'fullname': 'Author 124',
            'maxPaper': 0
        })

        self.assertEquals(response.status_code, 302)
        #Check if updated
        self.assertNotEquals(ConferenceChair.objects.first().email, "c123@gmail.com") 
        self.assertNotEquals(ConferenceChair.objects.first().username, "c123") 
        self.assertNotEquals(ConferenceChair.objects.first().password, "c123")  

        self.assertEquals(Author.objects.first().email,"a124@gmail.com")
        self.assertEquals(Author.objects.first().username,"a124")
        self.assertEquals(Author.objects.first().password,"a124")
        self.assertEquals(Author.objects.first().name,"Author 124")

    def test_updateConferenceRole_to_Reviewer_POST(self):
        #Sample Conference Chair Object
        self.conf1 = ConferenceChair.objects.create(
            email= "c123@gmail.com",
            username="c123",
            password="c123",
            name= "Conference 123"
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        #Update to Reviewer
        response = self.client.post(reverse('update_conference', args=[self.conf1.id]), {
            'roleList' :'Reviewer',
            'email' : 'r124@gmail.com',
            'username': 'r124',
            'password': 'r124',
            'fullname': 'Reviewer 124',
            'maxPaper': 124
        })

        self.assertEquals(response.status_code, 302)
        #Check if updated
        self.assertNotEquals(ConferenceChair.objects.first().email, "c123@gmail.com") 
        self.assertNotEquals(ConferenceChair.objects.first().username, "c123") 
        self.assertNotEquals(ConferenceChair.objects.first().password, "c123")  

        self.assertEquals(Reviewer.objects.first().email,"r124@gmail.com")
        self.assertEquals(Reviewer.objects.first().username,"r124")
        self.assertEquals(Reviewer.objects.first().password,"r124")
        self.assertEquals(Reviewer.objects.first().name,"Reviewer 124")
        self.assertEquals(Reviewer.objects.first().maxPaper, 124)

    def test_updateConferenceRole_to_Admin_POST(self):
        #Sample Conference Chair Object
        self.conf1 = ConferenceChair.objects.create(
            email= "c123@gmail.com",
            username="c123",
            password="c123",
            name= "Conference 123"
        )

        #Sample Session via Logging in
        session = self.client.session
        session['SysAdminLogged'] = "1"
        session.save()

        #Update to Admin
        response = self.client.post(reverse('update_conference', args=[self.conf1.id]), {
            'roleList' :'System Admin',
            'email' : 'sys124@gmail.com',
            'username': 'sys124',
            'password': 'sys124',
            'fullname': '-',
            'maxPaper': 0
        })

        self.assertEquals(response.status_code, 302)
        #Check if updated
        self.assertNotEquals(ConferenceChair.objects.first().email, "c123@gmail.com") 
        self.assertNotEquals(ConferenceChair.objects.first().username, "c123") 
        self.assertNotEquals(ConferenceChair.objects.first().password, "c123")   

        self.assertEquals(SystemAdmin.objects.first().email,"sys124@gmail.com")
        self.assertEquals(SystemAdmin.objects.first().username,"sys124")
        self.assertEquals(SystemAdmin.objects.first().password,"sys124")
    
    



