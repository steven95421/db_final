# Generated by Django 2.0.6 on 2018-06-24 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(help_text='Required. Inform a valid email address.', max_length=254, null=True),
        ),
    ]
