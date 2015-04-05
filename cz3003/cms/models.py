from django.db import models
from datetime import datetime  

# Create your models here.

#Abstract SensorData
class SensorData (models.Model):
	data = models.CharField(max_length = 200)
	time = models.DateTimeField (max_length = 200)
	type = models.CharField(max_length = 200)

#Map model
class Map (models.Model):
	
	name_location = models.CharField(max_length = 200)
	x_location = models.FloatField (default = 0.00)
	y_location = models.FloatField (default = 0.00)
	sensor = models.ForeignKey(SensorData)	

	def _str_(self):
		return self.name_location + "X: " + self.x_location + " Y: " + self.y_location


#GoogleMap model
class GoogleMap (Map):
	pass

#CallOperatorForm
class CallOperatorForm (models.Model):
	id_of_caller = models.CharField (max_length = 10)
	name_of_caller = models.CharField (max_length  = 200)
	contact_number = models.IntegerField (max_length = 20)
	nric = models.CharField (max_length = 10)
	content = models.CharField (max_length = 200)
	operator_id = models.CharField (max_length = 200)
	date = models.DateTimeField(default=datetime.now,blank=True)
	X_coordinate = models.DecimalField(max_digits=30, decimal_places=10)
	Y_coordinate = models.DecimalField(max_digits=30, decimal_places=10)
	severity_level = models.CharField (max_length  = 200)

	def _call_operator_form_(self):
		return 0

	def _submit_(self):
		return 0

#CrisisInstace
class CrisisInstance (models.Model):
	type_crisis  = models.CharField (max_length = 200)
	severity_level = models.CharField (max_length = 200)
	location_crisis = models.CharField (max_length  = 200)
	date_time = models.DateTimeField (max_length  = 200)
	content = models.CharField(max_length = 200)
	staff_id = models.CharField (max_length = 10)

	def _trigger_crisis_event(EventManager):
		return 0
		
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


#NEA inherit SensorData
class NEA (SensorData):
	pass
	
#Weather inherit SensorData
class Weather (SensorData):
	pass
#Event
class Event (models.Model):
	crisis_content = models.CharField (max_length = 200)
	event_time = models.DateField (max_length = 200)

#Account
class Account (models.Model):
	account_name = models.CharField (max_length = 200)

#Report
class Report (models.Model):
	crisis_instance = models.ForeignKey(CrisisInstance)

#MailMonitoring
class EmailMonitoring (models.Model):
	def _generate_report_(report):
		return report




	
	



