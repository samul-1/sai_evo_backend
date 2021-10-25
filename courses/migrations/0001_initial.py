# Generated by Django 3.2.8 on 2021-10-25 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('hidden', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('begin_timestamp', models.DateTimeField()),
                ('end_timestamp', models.DateTimeField()),
                ('event_type', models.PositiveIntegerField(choices=[(0, 'Self-service practice'), (1, 'In-class practice'), (2, 'Exam'), (3, 'Assignment')])),
                ('progression_rule', models.PositiveIntegerField(choices=[(0, 'All exercises at once'), (1, 'One at a time, can go back'), (2, 'One at a time, cannot go back')])),
                ('state', models.PositiveIntegerField(choices=[(0, 'Draft'), (1, 'Planned'), (2, 'Open'), (3, 'Closed')])),
            ],
        ),
        migrations.CreateModel(
            name='EventInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='EventInstanceSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_timestamp', models.DateTimeField(auto_now_add=True)),
                ('end_timestamp', models.DateTimeField(blank=True, null=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'In progress'), (1, 'Turned in')])),
                ('current_slot_index', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('public', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='EventTemplateRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('rule_type', models.PositiveSmallIntegerField(choices=[(0, 'Tag-based rule'), (1, 'Exercise ID-based rule')])),
            ],
        ),
        migrations.CreateModel(
            name='EventTemplateRuleClause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_type', models.PositiveSmallIntegerField(choices=[(0, 'Multiple choice single possible'), (1, 'Multiple choice multiple possible'), (2, 'Open answer'), (3, 'Completion'), (4, 'Aggregated'), (5, 'JavaScript'), (6, 'Attachment')])),
                ('text', models.TextField()),
                ('solution', models.TextField(blank=True)),
                ('draft', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exercises', to='courses.course')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_exercises', to='courses.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('correct', models.BooleanField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='courses.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipationAssessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Not graded'), (1, 'Partially graded'), (2, 'Fully graded')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipationSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipationSubmissionSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('seen_at', models.DateTimeField(blank=True, null=True)),
                ('answered_at', models.DateTimeField(blank=True, null=True)),
                ('answer_text', models.TextField(blank=True)),
                ('selected_choice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.exercisechoice')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='courses.participationsubmission')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipationAssessmentSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveSmallIntegerField()),
                ('comment', models.TextField(blank=True)),
                ('_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='courses.participationassessment')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseTestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('label', models.TextField(blank=True)),
                ('hidden', models.BooleanField(default=False)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testcases', to='courses.exercise')),
            ],
        ),
    ]
