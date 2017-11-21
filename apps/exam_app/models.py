# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def registration_validation(self, data):
        errors = {}
        if len(data['name']) < 2:
            errors['name'] = 'Name is incorrect'

        if len(data['alias']) < 2:
            errors['alias'] = 'Alias needs to be at least 2 characters'

        if len(data['password']) < 8:
            errors['password'] = 'Password needs to be at least 8 characters'
        
        if not data['password'] == data['confirm']:
            errors['password'] = 'Passwords do not match'

            # self.create(name=data['name'], alias=data['alias'], email_address=data['email'], password=data['password'], data = data['date'])

        return errors

class User(models.Model):
    name= models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email_address = models.CharField(max_length = 255, unique = True)
    password = models.CharField(max_length = 255)
    # dob = models.DateField(verbose_name=None)
    # message = models.CharField(max_length = 255)
    objects = UserManager()
    
class Message(models.Model):
    author = models.CharField(max_length = 255)
    message = models.TextField(max_length = 1000)
    user = models.ForeignKey(User, related_name='messages')
    # objects = UserManager()

# Create your models here.
