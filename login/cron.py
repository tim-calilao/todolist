from django_cron import CronJobBase, Schedule
from .models import todolist
from django.core.mail import send_mail
import time, datetime, pytz

class deadlineCheck(CronJobBase):
	RUN_EVERY_MINS = 1440 # every 24 hours

	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'deadlineCheck'    # a unique code

	def do(self):
		tdl = todolist.objects.all()
		todate = datetime.datetime.now()

		for i,c in enumerate(tdl):
			if tdl[i].deadline -  pytz.utc.localize(todate) <= datetime.timedelta(days=3) and tdl[i].completed == False:
				email_dict = {
					'd_activity' : tdl[i].activity,
					'd_username' : tdl[i].username,
					'd_notes' : tdl[i].notes,
					'd_deadline' : tdl[i].deadline,
				}
				email_subject = "To-do List Notification"
				email_message = "Hello "+str(tdl[i].username)+",\nThe activity "+str(tdl[i].activity)+" is less than 3 days away\n"+str(tdl[i].activity)+"'s deadline: "+str(tdl[i].deadline)+"\n"+str(tdl[i].activity)+"'s notes: "+str(tdl[i].notes)+"\nThis is an automated message so please don't reply to this email. If you want to stop receiving these notifications, login to your account and go to Settings. Under settings, leave the email address field blank and press 'Save'"
				email_from = "todolist.cpa@gmail.com"
				email_to = [str(User.objects.get(username__exact=tdl[i].username).email)]
				send_mail(email_subject, email_message, email_from, email_to, fail_silently=False)

