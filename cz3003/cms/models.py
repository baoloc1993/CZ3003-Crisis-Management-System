from django.db import models
from datetime import datetime  

# Create your models here.

#Abstract SensorData
class SensorData (models.Model):
	CRISIS_CHOICES = (
		('PSI', 'PSI'),
		('Wave speed', 'Wave speed'),
		('Water level', 'Water level'),
		('Earthquake level', 'Earthquake level'),)
	time = models.DateTimeField (default=datetime.now,blank=True)
	sensorType = models.CharField(max_length = 200, choices=CRISIS_CHOICES, unique=True)
	value = models.DecimalField(default = 0.00, max_digits=10, decimal_places=2)

	@classmethod
	def create(cls, sensorType, value):
		sensor=cls(sensorType = sensorType, value = value)
		return sensor

sensorPSI = SensorData.create('PSI', 150);
sensorWater = SensorData.create('Water level', 500);
sensorWave = SensorData.create('Wave speed', 10);
sensorEarth = SensorData.create('Earthquake level', 3.0);

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
	name_of_caller = models.CharField (max_length  = 200)
	contact_number = models.IntegerField (max_length = 20)
	nric = models.CharField (max_length = 10)
	content = models.CharField (max_length = 200)
	operator_id = models.CharField (max_length = 200)
	date = models.DateTimeField(default=datetime.now,blank=True)
	latitude = models.DecimalField(default = 1.3011873, max_digits=30, decimal_places=10)
	longitude = models.DecimalField(default = 103.8495055, max_digits=30, decimal_places=10)
	severity_level = models.CharField (max_length  = 200)
	status = models.SmallIntegerField()

	def _call_operator_form_(self):
		return 0

	def _submit_(self):
		return 0

#CrisisInstace
class CrisisInstance (models.Model):
	CRISIS_CHOICES = (
		('Tsunami', 'Tsunami'),
		('Haze', 'Haze'),)
	#'Haze', Tsunami
	crisisType = models.CharField(max_length = 200, choices=CRISIS_CHOICES)
	severity_level = models.CharField (max_length = 200)
	latitude = models.DecimalField(default = 1.3011873, max_digits=30, decimal_places=10)
	longitude = models.DecimalField(default = 103.8495055, max_digits=30, decimal_places=10)
	time = models.DateTimeField (default=datetime.now,blank=True)
	note = models.CharField(max_length = 200)
	staff_id = models.CharField (max_length = 10)
	CRISIS_STATUS = (
		('P', 'Pending'),
		('H', 'Happening'),
		('S', 'Stopped'))
	crisisStatus = models.CharField(default='Pending', max_length = 200, choices=CRISIS_STATUS)

	def _call_instance_(self):
		return 0
	def _trigger_crisis_event(EventManager):
		return 0
	def _submit_(self):
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




	
	



