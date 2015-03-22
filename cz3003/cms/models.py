from django.db import models

# Create your models here.

class Map (models.Model):
	name_location = models.CharField(max_length = 200)
	x_location = models.FloatField (default = 0.00)
	y_location = models.FloatField (default = 0.00)
	def _str_(self):
		return self.name_location + "X: " + self.x_location + " Y: " + self.y_location

class CallOperatorForm (models.Model):
	id_caller = models.CharField (max_length = 10)
	name_caller = models.CharField (max_length  = 200)
	contact_number = models.IntegerField (max_length = 20)
	nric = models.CharField (max_length = 10)
	content = models.CharField (max_length = 200)
	operator_id = models.CharField (max_length = 200)
	date_time = models.DateTimeField ('date published')
	location = models.CharField (max_length = 200)
	severity_level = models.CharField (max_length  = 200)

	def _call_operator_form_(self):
		return 0

class ReportForm (models.Model):
	type_crisis  = models.CharField (max_length = 200)
	severity_level = models.CharField (max_length = 200)
	location_crisis = models.CharField (max_length  = 200)
	date_time = models.DateTimeField (max_length  = 200)
	content = models.CharField(max_length = 200)
	staff_id = models.CharField (max_length = 10)
