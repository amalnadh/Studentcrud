from django.shortcuts import render,HttpResponse,redirect
from .forms import StudentForm
from .models import Student

# Create your views here.

def student(request):
    student=Student.objects.all()

    context={
        'studentlist':student
    }

    return render(request,'student.html',context)

    
def student_list(request):
    student=Student.objects.all()

    context={
        'studentlist':student
    }

    return render(request,'student_list.html',context)

def student_form(request,id=0):
    if request.method == 'GET':
        if id==0:
            form=StudentForm()
    
        else:
            student=Student.objects.get(pk=id)
            form=StudentForm(instance=student)

        return render(request,'student_form.html',{'form':form})
    else:
        if id==0:
            form = StudentForm(request.POST)
        else:   #updations
            student=Student.objects.get(pk=id)
            form=StudentForm(request.POST,instance=student)
        
        if form.is_valid():
            form.save()
        
        return redirect('/')


    

def delete(request,id):
    student=Student.objects.get(pk=id)
    student.delete()

    return redirect('/')

