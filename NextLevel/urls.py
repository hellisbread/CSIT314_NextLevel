"""NextLevel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from website import views, loginController, userController, authorController, systemAdminController, reviewerController, conferenceChairController
urlpatterns = [
    #General URL
    path('', loginController.index, name = 'index'),
    path('checkLogin/', loginController.checkLogin, name='login'),
    path('logout/', views.Logout, name = 'logout'),
    #Authors URL
    path('author/', authorController.authorPage, name = 'authorPage'),
    path('author/submitPaperPage/', authorController.submitPaperPage, name ='submitPaperPage'),
    path('author/viewPaperPage/', authorController.viewPaperPage, name='viewPaperPage'),
    path('author/viewPaperPage/deleteSubmittedPaper/<int:id>', authorController.deleteSubmittedPaper, name='deleteSubmittedPaper'),
    path('author/viewPaperPage/readSubmittedPaper/<int:id>', authorController.readSubmittedPaper, name = 'readSubmittedPaper'),
    path('author/viewPaperPage/updateSubmittedPaper/<int:id>', authorController.updateSubmittedPaper, name = 'updateSubmittedPaper'),
    #System Admins URL
    path('admin/', systemAdminController.systemAdminPage, name = 'systemAdminPage'),
    path('admin/create',userController.register, name='register'),
    path('admin/update_author/<int:id>', userController.updateAuthors, name='update_author'),
    path('admin/update_reviewer/<int:id>', userController.updateReviewers, name='update_reviewer'),
    path('admin/update_conference/<int:id>', userController.updateConfs, name='update_conference'),
    path('admin/update_admin/<int:id>', userController.updateAdmins, name='update_admin'),
    #Reviewer URL
    path('reviewer/', reviewerController.reviewerPage, name ='reviewerPage'),
    path('reviewer/bid/', reviewerController.bidPaper, name='bidPaper'),
    path('reviewer/bid/add/<int:id>', reviewerController.addBidPaper, name='addBidPaper'),
    path('reviewer/settings/', reviewerController.settings, name='settings'),
    path('reviewer/settings/update', reviewerController.updateSettings, name='updateSettings'),
    path('reviewer/papers/', reviewerController.biddedPaperPage, name='biddedPaper'),
    path('reviewer/papers/review/<int:id>',reviewerController.reviewPage,name='reviewPaper'),
    #Conference Chair URL
    path('conferenceChair/', conferenceChairController.conferenceChairPage, name = 'conferenceChairPage'),
    path('conferenceChair/viewBiddedPaper/', conferenceChairController.viewBiddedPaperPage, name ='viewBiddedPaperPage'),
    path('conferenceChair/viewBiddedPaper/allocatePaper/<int:id>',conferenceChairController.allocatePaper, name ='allocatePaper'),
    path('conferenceChair/viewBiddedPaper/decidePaper/<int:id>', conferenceChairController.decidePaper, name='decidePaper')
    
]
