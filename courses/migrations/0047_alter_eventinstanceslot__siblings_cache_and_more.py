# Generated by Django 4.0.4 on 2022-04-13 14:11

import courses.abstract_models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0046_eventinstanceslot__siblings_cache_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinstanceslot',
            name='_siblings_cache',
            field=models.JSONField(default=courses.abstract_models.get_default_sibling_cache),
        ),
        migrations.AlterField(
            model_name='participationassessmentslot',
            name='_siblings_cache',
            field=models.JSONField(default=courses.abstract_models.get_default_sibling_cache),
        ),
        migrations.AlterField(
            model_name='participationsubmissionslot',
            name='_siblings_cache',
            field=models.JSONField(default=courses.abstract_models.get_default_sibling_cache),
        ),
    ]
