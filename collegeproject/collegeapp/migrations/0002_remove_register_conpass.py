# Generated by Django 4.2.7 on 2023-11-11 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='conpass',
        ),
    ]
