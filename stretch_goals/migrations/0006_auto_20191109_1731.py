# Generated by Django 2.2.7 on 2019-11-09 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stretch_goals', '0005_record_goal_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_registered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='record',
            name='goal_number',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
