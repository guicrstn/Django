# Generated by Django 4.0.5 on 2022-06-22 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0011_client_delete_rendu'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='username',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
