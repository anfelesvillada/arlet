from django import forms
from latearrival.models import LateArrival

class LateArrivalForm(forms.ModelForm):
    class Meta:
        model = LateArrival
        fields = ["date_arrival","observations", "document_apprentice"]
        #personalizar campo fecha para que salga con el calendar
        widgets = {
            'date_arrival': forms.TextInput(attrs={'type': 'date'}),
        }
       