# Generated by Django 3.2.8 on 2021-11-01 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_alter_eventtemplate_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventparticipation',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(0, 'In progress'), (1, 'Turned in')], default=0),
        ),
        migrations.AlterField(
            model_name='eventtemplateruleclause',
            name='rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clauses', to='courses.eventtemplaterule'),
        ),
    ]
