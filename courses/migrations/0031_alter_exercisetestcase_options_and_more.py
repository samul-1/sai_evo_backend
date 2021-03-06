# Generated by Django 4.0.1 on 2022-03-01 16:20

from django.db import migrations, models
import django.db.models.constraints


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0030_exercisetestcase_testcase_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercisetestcase',
            options={'ordering': ['exercise_id', '_ordering']},
        ),
        migrations.RemoveConstraint(
            model_name='exercisetestcase',
            name='same_exercise_unique_testcase_code',
        ),
        migrations.AddField(
            model_name='exercisetestcase',
            name='_ordering',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='exercisetestcase',
            constraint=models.UniqueConstraint(deferrable=django.db.models.constraints.Deferrable['DEFERRED'], fields=('exercise_id', '_ordering'), name='same_exercise_unique_ordering_testcase'),
        ),
    ]
