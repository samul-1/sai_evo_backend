# Generated by Django 3.2.8 on 2021-11-01 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_auto_20211101_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventparticipation',
            name='assessment',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='participation', to='courses.participationassessment'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventparticipation',
            name='submission',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='participation', to='courses.participationsubmission'),
            preserve_default=False,
        ),
    ]