from django.contrib import admin
from cms.models import Map
from cms.models import GoogleMap
from cms.models import CallOperatorForm
from cms.models import CrisisInstance
from cms.models import SensorData
from cms.models import Event 
from cms.models import NEA
from cms.models import Weather
from cms.models import Event
from cms.models import Account
from cms.models import Report
from cms.models import EmailMonitoring





# Register your models here.
admin.site.register(GoogleMap)
admin.site.register(CallOperatorForm)
admin.site.register(CrisisInstance)
admin.site.register(Event)
admin.site.register(Account)
admin.site.register(NEA)
admin.site.register(Weather)
admin.site.register(Report)
admin.site.register(EmailMonitoring)

