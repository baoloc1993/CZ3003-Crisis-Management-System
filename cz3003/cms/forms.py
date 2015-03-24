from django import forms
from cms.models import CallOperatorForm
from datetime import datetime    

class MyForm(forms.ModelForm):
    class Meta:
        model = CallOperatorForm
        fields = ['id_of_caller', 'name_of_caller', 'contact_number', 'nric', 'content', 'operator_id', 'X_coordinate', 'Y_coordinate', 'severity_level']
