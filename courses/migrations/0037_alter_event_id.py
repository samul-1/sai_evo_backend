# Generated by Django 4.0.3 on 2022-03-30 08:32

from django.db import migrations
import hashid_field.field


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0036_exercisechoice_score_unselected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, prefix='', primary_key=True, serialize=False),
        ),
    ]
