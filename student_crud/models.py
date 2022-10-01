
from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    fullname=models.CharField(max_length=150)
    reg_no=models.CharField(max_length=10)
    mobile=models.CharField(max_length=10)
    email=models.EmailField()
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.fullname


