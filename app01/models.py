from django.db import models
from django.utils.timezone import now
import app01

# Create your models here.

class Users(models.Model):
    usr_name = models.CharField(max_length=255, primary_key=True)
    usr_password = models.CharField(max_length=25)
    usr_type = models.IntegerField()

    # 自定义表名
    # class Meta:
    #     db_table = 'Users'

class Worker(models.Model):
    worker_id = models.CharField(max_length=16, primary_key=True)
    worker_name = models.CharField(max_length=255)
    worker_sex = models.BooleanField()
    worker_age = models.IntegerField()
    # worker_department = models.ForeignKey(app01.models.Department, on_delete=models.SET_NULL)
    worker_department = models.CharField(max_length=255)
    worker_position = models.CharField(max_length=255)
    worker_phone = models.CharField(max_length=16)
    worker_entry_time = models.DateTimeField()

class Department(models.Model):
    department_name = models.CharField(max_length=255, primary_key=True)
    department_intro = models.TextField()

class Training(models.Model):
    training_id = models.CharField(max_length=16, primary_key=True)
    training_name = models.CharField(max_length=255)
    training_intro = models.TextField()
    training_place = models.CharField(max_length=255)
    training_start_time = models.DateTimeField()
    training_end_time = models.DateTimeField()

class Recruitment(models.Model):
    recruiter_id = models.CharField(max_length=16, primary_key=True)
    recruiter_name = models.CharField(max_length=255)
    recruiter_sex = models.BooleanField()
    recruiter_age = models.IntegerField()
    recruiter_target_department = models.CharField(max_length=255)
    recruiter_intro = models.TextField()
    recruiter_phone = models.CharField(max_length=16)

class Salary(models.Model):
    # worker_id = models.ForeignKey(app01.models.Worker, on_delete=models.CASCADE)
    worker_id = models.CharField(max_length=16, primary_key=True)
    salary = models.IntegerField()

class Reward(models.Model):
    # worker_id = models.ForeignKey(app01.models.Worker, on_delete=models.CASCADE)
    worker_id = models.CharField(max_length=16)
    reward = models.IntegerField()
    record = models.CharField(max_length=255)
