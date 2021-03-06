# Generated by Django 4.0.1 on 2022-03-01 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0027_alter_exercise_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercisetestcase',
            name='hidden',
        ),
        migrations.AlterField(
            model_name='event',
            name='_event_state',
            field=models.PositiveIntegerField(choices=[(0, 'Draft'), (1, 'Planned'), (2, 'Open'), (3, 'Closed'), (4, 'Restricted')], db_column='state', default=0),
        ),
    ]
