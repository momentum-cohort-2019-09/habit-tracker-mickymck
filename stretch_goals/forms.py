from django import forms
from stretch_goals.models import Goal


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        exclude = ['user', 'create_date']

