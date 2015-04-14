from django import forms
from cms.models import CallOperatorForm
from cms.models import CrisisInstance
from cms.models import SensorData
from datetime import datetime    

class MyIncidentForm(forms.ModelForm):
    class Meta:
        model = CallOperatorForm
        fields = ['name_of_caller', 'contact_number', 'nric', 'content', 'operator_id', 'latitude', 'longitude', 'severity_level', 'status']
    def clean_nric(self):
        data = self.cleaned_data['nric']
        if data == "S123456G":
            raise forms.ValidationError("This caller is in our black list!")
        if data == "S654321F":
            raise forms.ValidationError("This caller is in our black list!")
        return data

class MyCrisisForm(forms.ModelForm):
    class Meta:
        model = CrisisInstance
        fields = ['staff_id', 'crisisType', 'severity_level', 'latitude', 'longitude', 'note']

class MyNEAForm(forms.ModelForm):
    class Meta:
        model = SensorData
        fields = ['sensorType', 'value']
