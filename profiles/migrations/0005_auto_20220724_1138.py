# Generated by Django 3.1.14 on 2022-07-24 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20220724_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_surname',
        ),
    ]
