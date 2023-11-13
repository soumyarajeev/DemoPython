from django.db import models

# Create your models here.
# class Regapply(models.Model):
#     name=models.CharField(max_length=250,unique=True)
#     dob=models.SlugField(max_length=250,unique=True)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=250, unique=True)
#     phone = models.CharField(max_length=250, unique=True)
#     email = models.CharField(max_length=250, unique=True)
#     address = models.CharField(max_length=250, unique=True)
#     dept = models.CharField(max_length=250, unique=True)
#     course = models.CharField(max_length=250, unique=True)
#     purpose = models.CharField(max_length=250, unique=True)
#     materials = models.CharField(max_length=250, unique=True)
#
#
# class Department(models.Model):
#     name=models.CharField(max_length=250,unique=True)
#
# class Course(models.Model):
#     department = models.ForeignKey(Department,on_delete=models.CASCADE)
#     name=models.CharField(max_length=250,unique=True)
#




#
#     class Meta:
#         ordering=('name',)
#         verbose_name='department'
#         verbose_name_plural='departments'
#

#     class Meta:
#         ordering=('name',)
#         verbose_name='department'
#         verbose_name_plural='departments'