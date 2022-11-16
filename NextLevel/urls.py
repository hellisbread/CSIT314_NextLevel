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
from website.controllers.author import authorViewPaperController, authorSubmitPaperController, authorRateReviewController, authorViewReviewController, authorReadSubmittedPaperController, authorUpdateSubmittedPaperController

from website.controllers.reviewer import bidController, commentController, reviewController, settingsController, viewbiddedPaperController, CurrentReviewController
from website.controllers.conference_chair import CCviewReviewController, CCreadSubmittedPaperController, CCacceptOrRejectController, CCallocationPaperController

urlpatterns = [
    #General URL
    path('', loginController.index, name = 'index'),
    path('checkLogin/', loginController.checkLogin, name='login'),
    path('logout/', views.Logout, name = 'logout'),
    #Authors URL
    path('author/', authorViewPaperController.viewPaper, name='authorViewPaper'),
    path('author/submitPaper/', authorSubmitPaperController.submitPaper, name ='authorSubmitPaper'),
    path('author/submitPaper/create', authorSubmitPaperController.createPaper, name ='createAuthorPaper'),
    path('author/rateReview/', authorRateReviewController.rateReview, name = 'authorRateReview'),
    path('author/rateReview/create', authorRateReviewController.CreateReview, name='createAuthorRateReview'),
    path('author/rateReview/deleteReviewRating/<int:id>', authorRateReviewController.deleteReviewRating, name = 'authorDeleteReviewRating'),
    path('author/rateReview/viewReview/<int:id>', authorViewReviewController.viewReview, name="authorViewReview"),
    path('author/viewPaper/deleteSubmittedPaper/<int:id>', authorViewPaperController.deleteSubmittedPaper, name='authorDeleteSubmittedPaper'),
    path('author/viewPaper/readSubmittedPaper/<int:id>', authorReadSubmittedPaperController.readSubmittedPaper, name = 'authorReadSubmittedPaper'),
    path('author/viewPaper/updateSubmittedPaper/<int:id>', authorUpdateSubmittedPaperController.updateSubmittedPaperPage, name = 'authorUpdateSubmittedPaperPage'),
    path('author/viewPaper/updateSubmittedPaper/update/<int:id>', authorUpdateSubmittedPaperController.updateSubmittedPaper, name = 'authorUpdateSubmittedPaper'),
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
    path('reviewer/review/current/<int:id>',CurrentReviewController.currentReviews, name='currentReviews'),
    path('reviewer/review/comments/<int:bid_id>/<int:id>',commentController.commentPage, name='commentPage'),
    path('reviewer/review/comments/create/<int:bid_id>/<int:id>',commentController.createComment, name='createComment'),
    path('reviewer/review/comments/edit/<int:bid_id>',commentController.editComment, name='editComment'),
    path('reviewer/review/comments/delete/<int:bid_id>/<int:id>/<int:comment_id>',commentController.deleteComment, name='deleteComment'),
    #Conference Chair URL
    path('conferenceChair/allocationPaper/', CCallocationPaperController.allocationPaper, name ='CCallocationPaper'),
    path('conferenceChair/allocationPaper/allocatePaper/<int:id>',   CCallocationPaperController.allocatePaper, name ='CCallocatePaper'),
    path('conferenceChair/acceptOrReject/', CCacceptOrRejectController.acceptOrReject, name='CCacceptOrReject'),
    path('conferenceChair/acceptOrReject/readSubmittedPaper/<int:id>', CCreadSubmittedPaperController.readSubmittedPaper, name='CCreadSubmittedPaper'),
    path('conferenceChair/acceptOrReject/viewReview/<int:id>', CCviewReviewController.viewReview, name='CCviewReview'),
    
    
]
