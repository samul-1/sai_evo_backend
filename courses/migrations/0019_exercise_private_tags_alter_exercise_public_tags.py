# Generated by Django 4.0.1 on 2022-02-14 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_rename_tags_exercise_public_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='private_tags',
            field=models.ManyToManyField(blank=True, related_name='private_in_exercises', to='courses.Tag'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='public_tags',
            field=models.ManyToManyField(blank=True, related_name='public_in_exercises', to='courses.Tag'),
        ),
    ]
