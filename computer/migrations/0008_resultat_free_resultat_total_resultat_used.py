# Generated by Django 4.0.5 on 2022-06-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0007_resultat_delete_automate_delete_plateau'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultat',
            name='free',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='resultat',
            name='total',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='resultat',
            name='used',
            field=models.FloatField(default=None),
        ),
    ]
