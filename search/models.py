from django.db import models
from django.db.models.fields import IntegerField


class School(models.Model):
    school_name=models.CharField(max_length=255,blank=True, null=True)
    address=models.CharField(max_length=255,blank=True, null=True)
    class Meta:
        db_table = 'school'


class Student(models.Model):
    STATUS_CHOICES = (
        (0, '未毕业'),
        (1, '已毕业')
    )
    name=models.CharField(max_length=255,blank=True, null=True)
    school= models.ForeignKey(School, on_delete=models.CASCADE,related_name = "school_student",default='')
    telephone=models.BigIntegerField(blank=True, null=True)
    study_status=models.SmallIntegerField(choices=STATUS_CHOICES, default=0)
    class Meta:
        db_table = 'student'


