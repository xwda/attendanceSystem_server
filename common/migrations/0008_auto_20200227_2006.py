# Generated by Django 3.0.2 on 2020-02-27 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20200227_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='Course',
            new_name='course',
        ),
    ]