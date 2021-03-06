# Generated by Django 4.0.5 on 2022-07-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0065_remove_exercisechoice_score_unselected_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercisechoice',
            old_name='score_selected',
            new_name='correctness_percentage',
        ),
        migrations.AddField(
            model_name='exercise',
            name='child_weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
