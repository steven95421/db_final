# Generated by Django 2.0.6 on 2018-06-29 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='team_event',
            unique_together={('team_name', 'event')},
        ),
    ]
