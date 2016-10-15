from django.shortcuts import render
from .models import users,todolist
from .forms import SignUpForm, todolistForm, todolistEditForm, emailForm
from .tables import todolistTable
from django_tables2 import RequestConfig, A
from .forms import SignUpForm, todolistForm
from django.contrib.auth.models import User
import time, datetime, pytz
from django.core.mail import send_mail
from django import forms


# Create your views here.
def index(request):
	title = "Register"
	uname = " Guest."
	form_edit = todolistEditForm(request.POST or None)
	edit_act = request.POST.get('activity')
	smessage =  "Please login first."
	#form_edit.fields['activity'].choices = [('hello','hello'),('world','world')]
	#form_edit.fields['username'].value = str(request.user.username)
	form_edit.fields['username'].queryset = User.objects.filter(username__exact=str(request.user.username))
	print todolist.objects.filter(username__username=request.user.username).filter(activity__exact=request.POST.get('activity')).count()
	if request.POST and form_edit.is_valid and todolist.objects.filter(username__username=request.user.username).filter(activity__exact=request.POST.get('activity')).count():
		try:
			instance_edit = todolist.objects.get(activity=request.POST.get('activity'))
			form_edit = todolistEditForm(request.POST, instance = instance_edit)
			form_edit.save()
		except Exception as e:
		    print '%s (%s)' % (e.message, type(e))
	elif request.POST and form_edit.is_valid and not request.POST.get('activity')==None:
		instance = form_edit.save(commit=False)
		instance.save()
	

	if request.user.is_authenticated():
		table = todolistTable(todolist.objects.filter(username__username=str(request.user.username)))
		uname = str(request.user.username)
		smessage = ""
	else:
		table = todolistTable(todolist.objects.filter(username__username = ""))

	tdl = todolist.objects.all()
	todate = datetime.datetime.now()

	context = {
		"template_title" : title,
		"uname" : uname,
		'table' : table,
		'form_edit': form_edit,
		'smessage': smessage,
	}

	return render(request, 'index.php', context)

def sendMail(request):
	if request.POST:
		tdl = todolist.objects.all().order_by('username')
		todate = datetime.datetime.now()
		email_message=""
		ctr = 0
		for i,c in enumerate(tdl):
			email_message_h = "Hello "+str(tdl[i].username) +",\n"
			if tdl[i].completed == False and tdl[i].deadline -  pytz.utc.localize(todate) <= datetime.timedelta(days=3):
				if tdl[i].deadline <  pytz.utc.localize(todate):
					email_message += "The activity "+str(tdl[i].activity)+" is past its deadline.\n"+str(tdl[i].activity)+"'s deadline: "+str(tdl[i].deadline)+"\n"+str(tdl[i].activity)+"'s notes: "+str(tdl[i].notes)+"\nIf you've already completed this activity, kindly check 'completed' in the respective activity.\nThis is an automated message so please don't reply to this email. If you want to stop receiving these notifications, login to your account and go to Settings. Under settings, leave the email address field blank and press 'Save'\n\n"
				elif tdl[i].deadline -  pytz.utc.localize(todate) <= datetime.timedelta(days=3):
					email_message += "The activity "+str(tdl[i].activity)+" is less than 3 days away.\n"+str(tdl[i].activity)+"'s deadline: "+str(tdl[i].deadline)+"\n"+str(tdl[i].activity)+"'s notes: "+str(tdl[i].notes)+"\nThis is an automated message so please don't reply to this email. If you want to stop receiving these notifications, login to your account and go to Settings. Under settings, leave the email address field blank and press 'Save'\n\n"
				email_subject = "To-do List Notification"
				email_from = "todolist.cpa@gmail.com"
				email_to = [str(User.objects.get(username__exact=tdl[i].username).email)]
				send_mail(email_subject, email_message_h + email_message, email_from, email_to, fail_silently=True)
			
	return render(request, 'send.html',{})


def settings(request):
	context = {'message2' : ''}
	if request.user.is_authenticated():
		context['message'] = "This feature is currently disabled"
		context['message2'] = "An email notifying you 3 days prior to a deadline will be sent. If you want to turn off this function, simply remove your email address."
		form = emailForm(request.POST or None)
		context['form'] = form
		if User.objects.values_list('email', flat=True).get(username__exact=request.user.username):
			context['message'] = "This feature is currently enabled"

		if form.is_valid() and request.POST:
			instance = User.objects.get(username__exact=request.user.username)
			form = emailForm(request.POST, instance = instance)
			form.save()
			context['message'] = "This feature is currently disabled"
			if User.objects.values_list('email', flat=True).get(username__exact=request.user.username):
				context['message'] = "This feature is currently enabled"

			
	else:
		context['message'] = "Please Login first"

	return render(request, 'settings.php', context)

def deleteView(request):
	uname = "Guest."
	smessage = " Please login first."
	error_message = "There are currently no errors."
	error_activities = []
	if request.user.is_authenticated():
		smessage = ""
		uname = str(request.user.username)
		table = todolistTable(todolist.objects.filter(username__username=str(request.user.username)))
		if request.POST:
			del_list = str(request.POST.get('deleted')).split(';')
			if len(del_list) != len(set(del_list)):
				error_message="Please remove all duplicates."
			else:
				for d in del_list:
					try:
						todolist.objects.get(activity__exact=d.strip()).delete()
					except:
						if not request.POST.get('deleted') == "":
							error_message = "The following activities can't be found. Please check and try again."
							error_activities.append(str(d))
						else:
							error_message = "Please don't leave the text box blank."
	else:
		table = todolistTable(todolist.objects.filter(username__username=""))
	tdl = todolist.objects.filter(username__username=request.user.username)
	
	for i,c in enumerate(tdl):
		print tdl[i]

	

	context = {
		'table':table,
		'uname':uname,
		'error_message': error_message,
		'error_activities': error_activities,
		'smessage':  smessage,
	}
	return render(request,'delete.html',context)

# def tablesTable(request):	
# 	to_do_table = todolistTable(todolist.objects.all())
# 	context = {
# 		'table' : to_do_table
# 	}
# 	return render(request, 'tables.php', {'table' : todolistTable(todolist.objects.all())})

# def people(request):
#     return render(request, 'tables.php', {'people': Person.objects.all()})


