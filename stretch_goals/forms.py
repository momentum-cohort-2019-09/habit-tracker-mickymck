from django import forms
from stretch_goals.models import User, Goal, Record


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        exclude = ['user', 'create_date']

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['actual_number']

