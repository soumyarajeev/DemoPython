from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        uname=request.POST['username']
        passw=request.POST['password']
        user=auth.authenticate(username=uname,password=passw)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
           messages.info(request,"Invalid Credentials")
           return redirect('login')
    return render(request,"login.html")
def register(request):
        if request.method == 'POST':
            uname = request.POST['username']
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            email = request.POST['email']
            passw = request.POST['password']
            conpass = request.POST['password1']
            if passw == conpass:
                if User.objects.filter(username=uname).exists():
                    messages.info(request,"Username Already Exists")
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"Email Already Exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=email,
                                            password=passw)
                    user.save()
                    return redirect('login')
                    print("User Created")

            else:
                messages.info(request,"Password not matching")
                return redirect('register')
            return redirect('/')
        return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')