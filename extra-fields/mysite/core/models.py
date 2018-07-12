from __future__ import unicode_literals
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.db import models
from enum import Enum
'''class NewsCreationForm(models.Model):
    news_title = models.CharField(max_length=30)
    news_description = models.CharField(max_length=30)'''


class UserDetails(models.Model):

    class UserType(Enum):
        Employee = 'Employee'
        user = models.OneToOneField(User, related_name="username")


        #Admin = 'Admin'
        #

       # @classmethod
       # def as_tuple(cls):
       #     return ((item.value, item.name.replace('_','')) for item in cls)
