from django import forms
from django.forms import ModelForm
from stretch_goals.models import User, Goal, Record


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'nickname', 'greater_than', 'number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'ex: I will run more than 3 miles a day'
        self.fields['number'].widget.attrs['placeholder'] = 'ex: 3'
        self.fields['nickname'].widget.attrs['placeholder'] ='ex: miles'


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['actual_number']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

