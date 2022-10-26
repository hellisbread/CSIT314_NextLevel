from asyncio.windows_events import NULL
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Users(models.Model):
    email = models.EmailField(verbose_name='email address', max_length=255,unique=True, default=NULL)
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    Name = models.CharField(max_length = 255)

    class Meta:
        db_table = 'user'

    @classmethod
    def createUser(cls, email, username, password, Name):

        newUser = cls(email=email, username=username,password=password,Name = Name)

        newUser.save()

        return True

    def updateUser(self, email, username, password, Name):
        return self

class SystemAdmin(User):
    verified = models.BooleanField(default = False)
    approved = models.BooleanField(default = False)

    class Meta(User.Meta):
        db_table = 'system_admin'

class Author(User):
    verified = models.BooleanField(default = False)
    approved = models.BooleanField(default = False)

    class Meta(User.Meta):
        db_table = 'author'

class Reviewer(User):
    maxPaper = models.IntegerField(default = 0)
    verified = models.BooleanField(default = False)
    approved = models.BooleanField(default = False)

    class Meta(User.Meta):
        db_table = 'reviewer'

class ConferenceChair(User):
    verified = models.BooleanField(default = False)
    approved = models.BooleanField(default = False)

    class Meta(User.Meta):
        db_table = 'conference_chair'






