# Generated by Django 2.2.7 on 2019-11-07 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stretch_goals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='goal_number',
            field=models.PositiveIntegerField(default=None),
        ),
    ]
