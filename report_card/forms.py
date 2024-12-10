from django import forms
from .models import SubjectEntry

class SubjectEntryForm(forms.ModelForm):
    class Meta:
        model = SubjectEntry
        fields = ['student', 'ca1', 'ca2', 'exam']



class PinVerificationForm(forms.Form):
    admission_number = forms.CharField(max_length=50, label='Admission Number')
    pin = forms.CharField(max_length=6, label='PIN', widget=forms.PasswordInput)
