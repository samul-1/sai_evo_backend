# Generated by Django 3.2.9 on 2021-11-23 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourseprivilege',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='privileged_courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tag',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='courses.course'),
        ),
        migrations.AddField(
            model_name='participationsubmissionslot',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_slots', to='courses.participationsubmissionslot'),
        ),
        migrations.AddField(
            model_name='participationsubmissionslot',
            name='selected_choices',
            field=models.ManyToManyField(blank=True, to='courses.ExerciseChoice'),
        ),
        migrations.AddField(
            model_name='participationsubmissionslot',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='courses.participationsubmission'),
        ),
        migrations.AddField(
            model_name='participationassessmentslot',
            name='assessment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='courses.participationassessment'),
        ),
        migrations.AddField(
            model_name='participationassessmentslot',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_slots', to='courses.participationassessmentslot'),
        ),
        migrations.AddField(
            model_name='exercisetestcase',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testcases', to='courses.exercise'),
        ),
        migrations.AddField(
            model_name='exercisechoice',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='courses.exercise'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exercises', to='courses.course'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_exercises', to='courses.exercise'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='tags',
            field=models.ManyToManyField(blank=True, to='courses.Tag'),
        ),
        migrations.AddField(
            model_name='eventtemplateruleclause',
            name='rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clauses', to='courses.eventtemplaterule'),
        ),
        migrations.AddField(
            model_name='eventtemplateruleclause',
            name='tags',
            field=models.ManyToManyField(to='courses.Tag'),
        ),
        migrations.AddField(
            model_name='eventtemplaterule',
            name='exercises',
            field=models.ManyToManyField(blank=True, to='courses.Exercise'),
        ),
        migrations.AddField(
            model_name='eventtemplaterule',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rules', to='courses.eventtemplate'),
        ),
        migrations.AddField(
            model_name='eventtemplate',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_templates', to='courses.course'),
        ),
        migrations.AddField(
            model_name='eventtemplate',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventparticipation',
            name='assessment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participation', to='courses.participationassessment'),
        ),
        migrations.AddField(
            model_name='eventparticipation',
            name='event_instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participations', to='courses.eventinstance'),
        ),
        migrations.AddField(
            model_name='eventparticipation',
            name='submission',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participation', to='courses.participationsubmission'),
        ),
        migrations.AddField(
            model_name='eventparticipation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventinstanceslot',
            name='event_instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='courses.eventinstance'),
        ),
        migrations.AddField(
            model_name='eventinstanceslot',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.exercise'),
        ),
        migrations.AddField(
            model_name='eventinstanceslot',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_slots', to='courses.eventinstanceslot'),
        ),
        migrations.AddField(
            model_name='eventinstance',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='instances', to='courses.event'),
        ),
        migrations.AddField(
            model_name='eventinstance',
            name='exercises',
            field=models.ManyToManyField(blank=True, through='courses.EventInstanceSlot', to='courses.Exercise'),
        ),
        migrations.AddField(
            model_name='event',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='events', to='courses.course'),
        ),
        migrations.AddField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='events', to='courses.eventtemplate'),
        ),
        migrations.AddField(
            model_name='event',
            name='users_allowed_past_closure',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='courserole',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='courses.course'),
        ),
        migrations.AddField(
            model_name='course',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='enrolled_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='usercourseprivilege',
            constraint=models.UniqueConstraint(fields=('user_id', 'course_id'), name='same_course_unique_user_permission'),
        ),
        migrations.AddConstraint(
            model_name='tag',
            constraint=models.UniqueConstraint(fields=('course_id', 'name'), name='course_unique_tag_name'),
        ),
        migrations.AddConstraint(
            model_name='participationsubmissionslot',
            constraint=models.UniqueConstraint(fields=('submission_id', 'parent_id', 'slot_number'), name='participation_submission_unique_slot_number'),
        ),
        migrations.AddConstraint(
            model_name='participationassessmentslot',
            constraint=models.UniqueConstraint(fields=('assessment_id', 'parent_id', 'slot_number'), name='assessment_unique_slot_number'),
        ),
        migrations.AddConstraint(
            model_name='exercisetestcase',
            constraint=models.UniqueConstraint(fields=('exercise_id', 'code'), name='same_exercise_unique_testcase_code'),
        ),
        migrations.AddConstraint(
            model_name='exercise',
            constraint=models.UniqueConstraint(condition=models.Q(('parent__isnull', False)), fields=('parent_id', 'child_position'), name='same_parent_unique_child_position'),
        ),
        migrations.AddConstraint(
            model_name='eventtemplaterule',
            constraint=models.UniqueConstraint(fields=('template_id', 'target_slot_number'), name='template_unique_target_slot_number'),
        ),
        migrations.AddConstraint(
            model_name='eventinstanceslot',
            constraint=models.UniqueConstraint(fields=('event_instance_id', 'parent_id', 'slot_number'), name='event_instance_unique_slot_number'),
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.UniqueConstraint(fields=('course_id', 'name'), name='event_unique_name_course'),
        ),
        migrations.AddConstraint(
            model_name='courserole',
            constraint=models.UniqueConstraint(fields=('course_id', 'name'), name='same_course_unique_role_name'),
        ),
    ]
