import django_tables2 as tables
from .models import todolist
from table import Table
from table.columns import *

class todolistTable(Table):
	completed = CheckboxColumn(field = 'completed', header = "Completed", attrs = {'width' : '5%'})
	activity = Column(field = 'activity', header = "Activity")
	notes = Column(field = 'notes', header = "Notes", attrs = {'width' : '60%'})
	deadline = DatetimeColumn(field = 'deadline', header = "Deadline", attrs = {'width' : '10%'})
	class Meta:
		model = todolist
		attrs = {
			'class' : 'table table-striped',
		}
