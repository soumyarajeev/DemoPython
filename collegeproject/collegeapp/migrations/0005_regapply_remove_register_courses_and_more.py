# Generated by Django 4.2.7 on 2023-11-13 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regapply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('dob', models.SlugField(max_length=250, unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=250, unique=True)),
                ('phone', models.CharField(max_length=250, unique=True)),
                ('email', models.CharField(max_length=250, unique=True)),
                ('address', models.CharField(max_length=250, unique=True)),
                ('dept', models.CharField(max_length=250, unique=True)),
                ('course', models.CharField(max_length=250, unique=True)),
                ('purpose', models.CharField(max_length=250, unique=True)),
                ('materials', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='register',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='register',
            name='department',
        ),
        migrations.RemoveField(
            model_name='register',
            name='purpose',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Purpose',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
