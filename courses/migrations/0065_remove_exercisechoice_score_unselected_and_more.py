# Generated by Django 4.0.5 on 2022-07-13 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0064_event_time_limit_exceptions_event_time_limit_rule_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercisechoice',
            name='score_unselected',
        ),
        migrations.AddField(
            model_name='eventparticipationslot',
            name='populating_rule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='populated_slots', to='courses.eventtemplaterule'),
        ),
        migrations.AddField(
            model_name='eventtemplaterule',
            name='max_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
