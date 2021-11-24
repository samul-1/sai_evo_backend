# Generated by Django 3.2.9 on 2021-11-23 23:19

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='CourseRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('allow_privileges', models.JSONField(default=list)),
            ],
            options={
                'ordering': ['course_id', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('instructions', models.TextField(blank=True)),
                ('begin_timestamp', models.DateTimeField(blank=True, null=True)),
                ('end_timestamp', models.DateTimeField(blank=True, null=True)),
                ('event_type', models.PositiveIntegerField(choices=[(0, 'Self-service practice'), (1, 'In-class practice'), (2, 'Exam'), (3, 'Home assignment'), (4, 'External resource')])),
                ('state', models.PositiveIntegerField(choices=[(0, 'Draft'), (1, 'Planned'), (2, 'Open'), (3, 'Closed')], default=0)),
                ('exercises_shown_at_a_time', models.PositiveIntegerField(blank=True, null=True)),
                ('allow_going_back', models.BooleanField(default=True)),
                ('access_rule', models.PositiveIntegerField(choices=[(0, 'Allow'), (1, 'Deny')], default=0)),
                ('access_rule_exceptions', models.JSONField(blank=True, default=list)),
            ],
            options={
                'ordering': ['course_id', 'pk'],
            },
        ),
        migrations.CreateModel(
            name='EventInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ['event_id', 'pk'],
            },
        ),
        migrations.CreateModel(
            name='EventInstanceSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_number', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['event_instance_id', 'slot_number'],
            },
        ),
        migrations.CreateModel(
            name='EventParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_timestamp', models.DateTimeField(auto_now_add=True)),
                ('end_timestamp', models.DateTimeField(blank=True, null=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'In progress'), (1, 'Turned in')], default=0)),
                ('current_slot_cursor', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['begin_timestamp', 'pk'],
            },
        ),
        migrations.CreateModel(
            name='EventTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('public', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['course_id', 'pk'],
            },
        ),
        migrations.CreateModel(
            name='EventTemplateRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_type', models.PositiveSmallIntegerField(choices=[(0, 'Tag-based rule'), (1, 'Exercise ID-based rule'), (2, 'Fully random choice')])),
                ('target_slot_number', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['template_id', 'target_slot_number'],
            },
        ),
        migrations.CreateModel(
            name='EventTemplateRuleClause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_position', models.PositiveIntegerField(blank=True, null=True)),
                ('exercise_type', models.PositiveSmallIntegerField(choices=[(0, 'Multiple choice, single possible'), (1, 'Multiple choice, multiple possible'), (2, 'Open answer'), (3, 'Completion'), (4, 'Aggregated'), (5, 'JavaScript'), (6, 'Attachment')])),
                ('label', models.CharField(blank=True, max_length=75)),
                ('text', models.TextField(blank=True)),
                ('solution', models.TextField(blank=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Draft'), (1, 'Private'), (2, 'Public')], default=2)),
                ('time_to_complete', models.PositiveIntegerField(blank=True, null=True)),
                ('skip_if_timeout', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['course_id', django.db.models.expressions.OrderBy(django.db.models.expressions.F('parent_id'), nulls_first=True), django.db.models.expressions.OrderBy(django.db.models.expressions.F('child_position'), nulls_first=True), 'pk'],
            },
        ),
        migrations.CreateModel(
            name='ExerciseChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('score', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            options={
                'ordering': ['exercise_id', 'pk'],
            },
        ),
        migrations.CreateModel(
            name='ExerciseTestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('label', models.TextField(blank=True)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['exercise_id', 'pk'],
            },
        ),
        migrations.CreateModel(
            name='ParticipationAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.PositiveIntegerField(choices=[(0, 'Draft'), (1, 'For review'), (2, 'Published')], default=0)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='ParticipationAssessmentSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_number', models.PositiveIntegerField()),
                ('comment', models.TextField(blank=True)),
                ('_score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
            options={
                'ordering': ['assessment_id', 'slot_number'],
            },
        ),
        migrations.CreateModel(
            name='ParticipationSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='ParticipationSubmissionSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_number', models.PositiveIntegerField()),
                ('seen_at', models.DateTimeField(blank=True, null=True)),
                ('answered_at', models.DateTimeField(blank=True, null=True)),
                ('answer_text', models.TextField(blank=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'ordering': ['submission_id', 'slot_number'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'ordering': ['course_id', 'pk'],
            },
        ),
        migrations.CreateModel(
            name='UserCoursePrivilege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_privileges', models.JSONField(blank=True, default=list)),
                ('deny_privileges', models.JSONField(blank=True, default=list)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='privileged_users', to='courses.course')),
            ],
        ),
    ]
