# Generated by Django 4.0.1 on 2022-03-01 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0029_rename_label_exercisetestcase_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercisetestcase',
            name='testcase_type',
            field=models.PositiveIntegerField(choices=[(0, 'Show both code and text'), (1, 'Show text only'), (2, 'Hidden')], default=0),
        ),
    ]
