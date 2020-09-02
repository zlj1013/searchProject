from django.db import models
from django.db.models.fields import IntegerField


class School(models.Model):
    '''
    学校表设计
    '''
    id = models.AutoField(primary_key=True)
    school_name=models.CharField(max_length=255,blank=True, null=True)
    address=models.CharField(max_length=255,blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'school'
    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.school_name


class Student(models.Model):
    '''
    学生表设计
    '''
    #id = models.AutoField(max_length=11,primary_key=True)
    STATUS_CHOICES = (
        (0, '未毕业'),
        (1, '已毕业')
    )
    name=models.CharField(max_length=255,blank=True, null=True)
    #school_id=models,IntegerField(max_length=11,blank=True, null=True)
    school= models.ForeignKey(School, on_delete=models.CASCADE,
                                  related_name = "school_student",default='')
    telephone=models.BigIntegerField(blank=True, null=True)
    study_status=models.SmallIntegerField(choices=STATUS_CHOICES, default=0)
    class Meta:
        managed = True
        db_table = 'student'
    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.nam


class Text(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'text'