from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.

def signup(request):

    if request.method == 'POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User name already taken')
                return redirect('signup')

            elif  User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)

                user.save()
                # messages.info(request,'User created Successfully')
                return redirect('signin')
        else:
            messages.info(request,'Password not Matching')
            return redirect('signup')


    return render(request,'signup.html')



def signin(request):

    if request.method=='POST':

        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)

            return redirect('student_list')
        else:
            messages.info(request,'Invalid Username Or Password')

            return redirect('signin')

    return render(request,'signin.html')


def signout(request):

    auth.logout(request)


    return redirect('/')
