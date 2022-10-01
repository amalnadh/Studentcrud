from dataclasses import fields
from django import forms
from .models import Course,Student

class StudentForm(forms.ModelForm):


    class Meta:
        model=Student
        fields=('fullname','reg_no','mobile','email','course_name')
        labels={
            'fullname':'full Name:',
            'reg_no':'Reg. No:',
            'email':'Email'

        }