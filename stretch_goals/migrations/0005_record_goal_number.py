# Generated by Django 2.2.7 on 2019-11-07 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stretch_goals', '0004_remove_record_goal_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='goal_number',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
