# Generated by Django 4.0.1 on 2022-01-14 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_tag_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisechoice',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
