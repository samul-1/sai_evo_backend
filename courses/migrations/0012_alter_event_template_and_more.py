# Generated by Django 4.0.1 on 2022-01-29 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_alter_eventtemplaterule_rule_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='template',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.eventtemplate'),
        ),
        migrations.AlterField(
            model_name='eventparticipation',
            name='current_slot_cursor',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
