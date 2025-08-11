from django.db import models

from django.db.models import Model

class CourseModel(models.Model):
    name = models.CharField(max_length=30)
    base=models.CharField(max_length=30)
    website_link=models.CharField(max_length=30)

class TestModel(models.Model):
    name = models.CharField(max_length=30)
    courseid=models.CharField(max_length=30)

class QuestionModel(models.Model):
    name = models.CharField(max_length=30)
    testid=models.CharField(max_length=30)

class StudentModel(Model):
    username=models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)

class ScholarshipModel(Model):
    name=models.CharField(max_length=50)
    stateorcentral=models.CharField(max_length=50)
    tenthper=models.CharField(max_length=50)
    twelvethper=models.CharField(max_length=50)
    cast=models.CharField(max_length=50)
    sport=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    income=models.CharField(max_length=50)
    isdisable=models.CharField(max_length=50)
    lastdate=models.CharField(max_length=50)

class SoftSkillsModel(Model):
    title=models.CharField(max_length=50)
    link=models.CharField(max_length=50)