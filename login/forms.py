from django import forms
from django.db import models
from .models import users, todolist
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(widget=forms.PasswordInput)
	username = forms.CharField(max_length = 256)
	class Meta:
		model = users
		fields = ['username','password','confirm_password']

	def clean_username(self):
		username  = self.cleaned_data.get('username')
		if username and users.objects.filter(username=username).count():
			raise forms.ValidationError(u'Username is already taken.')
		return username
	def clean_password(self):
		password = self.cleaned_data.get('password')
		print self.cleaned_data.get('confirm_password')
		if password and password != self.cleaned_data.get('confirm_password'):
			raise forms.ValidationError(u'Password and Confirm Password does not match.')
		return password

class todolistForm(forms.ModelForm):
	class Meta:
		model = todolist
		fields = ["username", "completed", "activity", "notes", "deadline"]

class todolistEditForm(forms.ModelForm):
	class Meta:
		model = todolist
		fields = ["username","activity","completed", "notes", "deadline"]

	#username = forms.CharField(max_length=255, disabled = True)
	username = forms.ModelChoiceField(queryset=User.objects.all())
	completed = models.BooleanField()
	activity = models.CharField(max_length = 256, null = True, blank = False)
	notes = models.TextField(max_length = 10000, null = True, blank = False)
	deadline = forms.DateTimeField()

	def clean_activity(self):
		activity = self.cleaned_data.get('activity')
		if ';' in activity:
			raise forms.ValidationError(u'Activity name cannot contain semi-colon(s).')

		return activity

class emailForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["email"]



