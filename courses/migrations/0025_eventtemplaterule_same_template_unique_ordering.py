# Generated by Django 4.0.1 on 2022-02-16 19:20

from django.db import migrations, models
import django.db.models.constraints


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_remove_exercisechoice_same_exercise_unique_ordering_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='eventtemplaterule',
            constraint=models.UniqueConstraint(deferrable=django.db.models.constraints.Deferrable['DEFERRED'], fields=('template_id', '_ordering'), name='same_template_unique_ordering'),
        ),
    ]
