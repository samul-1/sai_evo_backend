# Generated by Django 4.0.1 on 2022-01-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_alter_event_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtemplaterule',
            name='rule_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Tag-based rule'), (1, 'Exercise ID-based rule'), (2, 'Fully random choice')], null=True),
        ),
    ]
