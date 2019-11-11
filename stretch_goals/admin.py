from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from stretch_goals.models import User, Goal, Record

# Register your models here.

class RecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal', 'goal_number', 'actual_number', 'date')


admin.site.register(User, UserAdmin)
admin.site.register(Goal)
admin.site.register(Record, RecordAdmin)

