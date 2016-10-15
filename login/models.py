from __future__ import unicode_literals
from django.contrib.auth.models import User
from django import forms

from django.db import models

# Create your models here.
class users(models.Model):
	email = models.EmailField(null = True, blank=False)
	password = models.CharField(max_length = 256, null = True, blank=False)
	#models.DateTimeField()
	#models.DateField()
	#models.TimeField()

	def __unicode__(self):
		return self.activity

class todolist(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	completed = models.BooleanField()
	activity = models.CharField(max_length = 256, primary_key=True)
	notes = models.TextField(max_length = 10000, null = True, blank = False)
	deadline = models.DateTimeField(auto_now = False, auto_now_add = False, blank = True)

	def __unicode__(self):
		return str(self.activity)

	# def clean_activity(self):
	# 	act = self.cleaned_data['activity']

