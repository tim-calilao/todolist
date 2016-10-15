from django.contrib import admin
from .models import users, todolist
from .forms import SignUpForm, todolistForm
# Register your models here.

class usersAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","password"]
	form = SignUpForm
	# class Meta:
	# 	model = users

admin.site.register(users, usersAdmin)

class todolistAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "username", "completed", "activity", "notes", "deadline"]
	form = todolistForm

admin.site.register(todolist, todolistAdmin)