from django import forms
from .widgets import GenderIconWidget

class BMIForm(forms.Form):
    height = forms.IntegerField(label="Height (cm)", min_value=20, max_value=230,initial=20)
    #age = forms.IntegerField(label="Age")
    #weight = forms.IntegerField(label="Weight (KG)")
    