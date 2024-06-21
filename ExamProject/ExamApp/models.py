from django.db import models

# Create your models here.


class StudentInfo(models.Model):
    FullName=models.CharField(max_length=100,null=True)
    Matric=models.CharField(max_length=100,null=True)
    Picture=models.ImageField(blank=True,null=True,upload_to='Student Profile')
    Department=models.CharField(max_length=100,null=True)
    DOB=models.CharField(max_length=100,null=True)
    Announcement=models.CharField(max_length=100,null=True)

class Courses(models.Model):
    Course_Title=models.CharField(max_length=200,null=True)  
    Course_Code=models.CharField(max_length=200,null=True)
    Department=models.CharField(max_length=200,null=True)
    
class Registered_Courses(models.Model):
    Matric=models.CharField(max_length=200,null=True)
    Course=models.CharField(max_length=200,null=True)
    Department=models.CharField(max_length=100,null=True)
class CurrentExam(models.Model):
    Department=models.CharField(max_length=100,null=True)
    Course=models.CharField(max_length=100,null=True)
    Date=models.CharField(max_length=100,null=True)
    Venue=models.CharField(max_length=100,null=True)
