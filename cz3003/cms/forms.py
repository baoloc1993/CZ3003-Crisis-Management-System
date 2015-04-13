from django import forms
from cms.models import CallOperatorForm
from cms.models import CrisisInstance
from cms.models import SensorData
from datetime import datetime    

class MyIncidentForm(forms.ModelForm):
    class Meta:
        model = CallOperatorForm
        fields = ['name_of_caller', 'contact_number', 'nric', 'content', 'operator_id', 'latitude', 'longitude', 'severity_level', 'status']

class MyCrisisForm(forms.ModelForm):
    class Meta:
        model = CrisisInstance
        fields = ['staff_id', 'crisisType', 'severity_level', 'latitude', 'longitude', 'note']

class MyNEAForm(forms.ModelForm):
    class Meta:
        model = SensorData
        fields = ['sensorType', 'value']
