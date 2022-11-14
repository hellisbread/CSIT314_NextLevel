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

from website import views, loginController, authorController, conferenceChairController

from website.controllers.system_admin import updateAuthorController, updateAdminController, updateConferenceController, updateReviewerController, createUserController, systemAdminController
from website.controllers.author import submitPaperController, viewPaperController, rateReviewController, authorViewReviewController
from website.controllers.reviewer import bidController, commentController, reviewController, settingsController, viewbiddedPaperController
from website.controllers.conference_chair import CCviewReviewController

urlpatterns = [
    #General URL
    path('', loginController.index, name = 'index'),
    path('checkLogin/', loginController.checkLogin, name='login'),
    path('logout/', views.Logout, name = 'logout'),
    #Authors URL
    path('author/', authorController.authorPage, name = 'authorPage'),
    path('author/submitPaperPage/', submitPaperController.submitPaperPage, name ='submitPaperPage'),
    path('author/viewPaperPage/', viewPaperController.viewPaperPage, name='viewPaperPage'),
    path('author/rateReviewPage/', rateReviewController.rateReview, name = 'rateReview'),
    path('author/rateReviewPage/deleteReviewRating/<int:id>', rateReviewController.deleteReviewRating, name = 'deleteReviewRating'),
    path('author/rateReviewPage/viewReview/<int:id>', authorViewReviewController.viewReview, name="authorViewReview"),
    path('author/viewPaperPage/deleteSubmittedPaper/<int:id>', viewPaperController.deleteSubmittedPaper, name='deleteSubmittedPaper'),
    path('author/viewPaperPage/readSubmittedPaper/<int:id>', viewPaperController.readSubmittedPaper, name = 'readSubmittedPaper'),
    path('author/viewPaperPage/updateSubmittedPaper/<int:id>', viewPaperController.updateSubmittedPaper, name = 'updateSubmittedPaper'),
    #System Admins URL
    path('admin/', systemAdminController.systemAdminPage, name = 'systemAdminPage'),
    path('admin/create',createUserController.createNewUser, name='register'),
    path('admin/update_author/<int:id>', updateAuthorController.updateAuthors, name='update_author'),
    path('admin/update_reviewer/<int:id>', updateReviewerController.updateReviewers, name='update_reviewer'),
    path('admin/update_conference/<int:id>', updateConferenceController.updateConfs, name='update_conference'),
    path('admin/update_admin/<int:id>', updateAdminController.updateAdmins, name='update_admin'),
    #Reviewer URL
    path('reviewer/', viewbiddedPaperController.biddedPaperPage, name='biddedPaper'),
    path('reviewer/bid/', bidController.bidPaper, name='bidPaper'),
    path('reviewer/bid/add/<int:id>', bidController.addBidPaper, name='addBidPaper'),
    path('reviewer/bid/delete/<int:id>', bidController.deleteBidPaper, name='deleteBidPaper'),
    path('reviewer/settings/', settingsController.settings, name='settings'),
    path('reviewer/settings/update', settingsController.updateSettings, name='updateSettings'),
    path('reviewer/review/<int:id>',reviewController.reviewPage, name='reviewPaper'),
    path('reviewer/review/create/<int:id>',reviewController.createReview, name='createReview'),
    path('reviewer/review/edit/<int:id>',reviewController.editReview, name='editReview'),
    path('reviewer/review/delete/<int:id>',reviewController.deleteReview, name='deleteReview'),
    path('reviewer/review/comments/<int:id>',commentController.commentPage, name='commentPage'),
    path('reviewer/review/comments/create/<int:id>',commentController.createComment, name='createComment'),
    path('reviewer/review/comments/edit',commentController.editComment, name='editComment'),
    path('reviewer/review/comments/delete/<int:id>/<int:comment_id>',commentController.deleteComment, name='deleteComment'),
    #Conference Chair URL
    path('conferenceChair/', conferenceChairController.conferenceChairPage, name = 'conferenceChairPage'),
    path('conferenceChair/allocationPaper/', conferenceChairController.allocationPaper, name ='allocationPaper'),
    path('conferenceChair/allocationPaper/allocatePaper/<int:id>',conferenceChairController.allocatePaper, name ='allocatePaper'),
    path('conferenceChair/acceptOrReject/', conferenceChairController.acceptOrReject, name='acceptOrReject'),
    path('conferenceChair/acceptOrReject/readSubmittedPaper/<int:id>', conferenceChairController.readSubmittedPaper, name='CCreadSubmittedPaper'),
    path('conferenceChair/acceptOrReject/viewReview/<int:id>', CCviewReviewController.viewReview, name='CCviewReview'),
    
    
]
