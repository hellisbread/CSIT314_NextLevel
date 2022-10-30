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

from website import views, loginController, userController, authorController, systemAdminController

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', views.loginView, name='login'),
    path('', loginController.index, name = 'index'),
    path('db/', userController.db, name='db'),
    path('register/', userController.register, name='register'),
    path('register/addNewUser/', userController.addNewUser, name = 'addNewUser'),
    path('update/<int:id>', userController.update, name='update'),
    path('update/updateProfile/<int:id>', userController.updateProfile, name='update'),
    path('checkLogin/', loginController.checkLogin, name='login'),
    path('logout/', views.Logout, name = 'logout'),
    path('author/', authorController.authorPage, name = 'authorPage'),
    path('author/submitPaperPage/', authorController.submitPaperPage, name ='submitPaperPage'),
    path('author/viewPaperPage/', authorController.viewPaperPage, name='viewPaperPage'),
    path('author/viewPaperPage/deleteSubmittedPaper/<int:id>', authorController.deleteSubmittedPaper, name='deleteSubmittedPaper'),
    path('author/viewPaperPage/readSubmittedPaper/<int:id>', authorController.readSubmittedPaper, name = 'readSubmittedPaper'),
    path('author/viewPaperPage/updateSubmittedPaper/<int:id>', authorController.updateSubmittedPaper, name = 'updateSubmittedPaper'),
    path('systemAdmin/', systemAdminController.systemAdminPage, name = 'systemAdminPage')
]
