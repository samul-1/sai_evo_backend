# Generated by Django 3.2.8 on 2021-10-25 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tags.Tag'),
        ),
        migrations.AddField(
            model_name='eventtemplateruleclause',
            name='rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.eventtemplaterule'),
        ),
        migrations.AddField(
            model_name='eventtemplateruleclause',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag'),
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
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventparticipation',
            name='assessment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.participationassessment'),
        ),
        migrations.AddField(
            model_name='eventparticipation',
            name='event_instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participations', to='courses.eventinstance'),
        ),
        migrations.AddField(
            model_name='eventparticipation',
            name='submission',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.participationsubmission'),
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='courses.exercise'),
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
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='events', to='courses.eventtemplate'),
        ),
        migrations.AddField(
            model_name='course',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
