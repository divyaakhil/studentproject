from django.db import models

# Create your models here.
class Course(models.Model):
    coursename=models.CharField(max_length=255)
    coursefee=models.IntegerField()
    def __str__(self):
        return self.coursename   
class Student(models.Model):
    studentname=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    age=models.IntegerField(null=True,blank=True,default=1)
    jdate=models.DateField()  
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.studentname  
      