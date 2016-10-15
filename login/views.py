from django.shortcuts import render
from .models import users,todolist
from .forms import SignUpForm, todolistForm, todolistEditForm, emailForm
from .tables import todolistTable
from django_tables2 import RequestConfig, A
from .forms import SignUpForm, todolistForm
from django.contrib.auth.models import User
import time, datetime, pytz
from django.core.mail import send_mail


# Create your views here.
def index(request):
	title = "Register"
	form_edit = todolistEditForm(request.POST or None)
	edit_act = request.POST.get('activity')
	#form_edit.fields['activity'].choices = [('hello','hello'),('world','world')]
	#form_edit.fields['username'].value = str(request.user.username)
	form_edit.fields['username'].queryset = User.objects.filter(username__exact=str(request.user.username))

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
	else:
		table = todolistTable(todolist.objects.filter(username__username = ""))
		uname = "Guest. Please login first."

	context = {
		"template_title" : title,
		"uname" : uname,
		'table' : table,
		'form_edit': form_edit,
	}

	return render(request, 'index.php', context)

# def tables(request):
# 	table = todolistTable(todolist.objects.filter(username__username = ""))
# 	context = {'table' : table}
	
# 	return render(request, 'tables.php', context)


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

			
	else:
		context['message'] = "Please Login first"

	return render(request, 'settings.php', context)

# def tablesTable(request):	
# 	to_do_table = todolistTable(todolist.objects.all())
# 	context = {
# 		'table' : to_do_table
# 	}
# 	return render(request, 'tables.php', {'table' : todolistTable(todolist.objects.all())})

# def people(request):
#     return render(request, 'tables.php', {'people': Person.objects.all()})


