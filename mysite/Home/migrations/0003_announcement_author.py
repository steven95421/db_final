# Generated by Django 2.0.6 on 2018-06-24 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20180527_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='author',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
