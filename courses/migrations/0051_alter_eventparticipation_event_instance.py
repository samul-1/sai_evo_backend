# Generated by Django 4.0.4 on 2022-04-15 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0050_alter_eventparticipation_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventparticipation',
            name='event_instance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='participations', to='courses.eventinstance'),
        ),
    ]
