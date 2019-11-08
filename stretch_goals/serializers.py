from stretch_goals.models import User, Goal, Record
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class GoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goal
        fields = ['user', 'name', 'nickname', 'greater_than', 'number', 'create_date']

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ['user', 'goal', 'actual_number', 'goal_number', 'datetime']

