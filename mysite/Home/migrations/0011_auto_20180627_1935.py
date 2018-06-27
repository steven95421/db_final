# Generated by Django 2.0.6 on 2018-06-27 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_auto_20180626_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_event',
            fields=[
                ('team', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=100)),
                ('event_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team_member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=2000)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Home.Team_event')),
            ],
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
