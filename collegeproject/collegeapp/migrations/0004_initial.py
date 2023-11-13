# Generated by Django 4.2.7 on 2023-11-12 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('collegeapp', '0003_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'departments',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'purpose',
                'verbose_name_plural': 'purposes',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('dob', models.CharField(max_length=250, unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=250, unique=True)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=250, unique=True)),
                ('address', models.CharField(max_length=250, unique=True)),
                ('material', models.CharField(max_length=250, unique=True)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeapp.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeapp.department')),
                ('purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeapp.purpose')),
            ],
            options={
                'verbose_name': 'register',
                'verbose_name_plural': 'registers',
                'ordering': ('name',),
            },
        ),
    ]