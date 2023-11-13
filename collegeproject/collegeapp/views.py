from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def allDept(request):
    dept_list=none
    dept_list = Department.objects.all().filter(available=True)


def demo(request):
    return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passw = request.POST['password']
        user=auth.authenticate(username=uname,password=passw)
        if user is not None:
            auth.login(request,user)
            return redirect('about')
        else:
            messages.info(request, "Invalid Username")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passw = request.POST['password']
        conpass = request.POST['conpass']
        if passw == conpass :
            user = User.objects.create_user(username=uname, password=passw)
            user.save()
            print("USER CREATED")
        else:
            messages.info(request,"Password Not Matching")
        return redirect('login')
    return render(request,"register.html")

def about(request):
    return render(request,"about.html")

def apply(request):
    return render(request,"apply.html")

def logout(request):
    auth.logout(request)
    return redirect('/')