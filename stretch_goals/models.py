from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User (AbstractUser):
    # follower = models.ManyToManyField(to='User', null=True, blank=True, related_name='followers')

    def __str__(self):
        return self.username

class Goal (models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, related_name='goals')
    name = models.TextField(max_length=255)
    nickname = models.CharField(max_length=100)
    greater_than = models.BooleanField()
    number = models.PositiveIntegerField()
    create_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nickname

class Record (models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, related_name='records')
    goal = models.ForeignKey(to=Goal, on_delete=models.CASCADE, blank=True, null=True, related_name='records')
    goal_number = None
    actual_number = models.PositiveIntegerField()
    datetime = models.DateTimeField(default=timezone.now)

