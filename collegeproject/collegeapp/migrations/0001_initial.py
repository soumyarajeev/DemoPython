# Generated by Django 4.2.7 on 2023-11-11 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=250)),
                ('passw', models.CharField(max_length=250)),
                ('conpass', models.CharField(max_length=250)),
            ],
        ),
    ]
