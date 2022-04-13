# Generated by Django 4.0.4 on 2022-04-13 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0047_alter_eventinstanceslot__siblings_cache_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventinstanceslot',
            name='_siblings_cache',
        ),
        migrations.RemoveField(
            model_name='participationassessmentslot',
            name='_siblings_cache',
        ),
        migrations.RemoveField(
            model_name='participationsubmissionslot',
            name='_siblings_cache',
        ),
        migrations.AddField(
            model_name='participationassessmentslot',
            name='_submission_sibling',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.participationsubmissionslot'),
        ),
        migrations.AddField(
            model_name='participationsubmissionslot',
            name='_assessment_sibling',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.participationassessmentslot'),
        ),
    ]
