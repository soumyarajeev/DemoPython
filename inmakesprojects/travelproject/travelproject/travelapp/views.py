from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from . models import Place
from . models import Team
# Create your views here.
def demo(request):
    res=Place.objects.all()
    obj=Team.objects.all()
    return render(request,"index.html",{'result':res,'flower':obj})
    # dist="Alappuzha"
    # return render(request,"home1.html",{'dis':dist})

# def addition(request):
#     n1=int(request.GET['num1'])
#     n2=int(request.GET['num2'])
#     res=n1+n2
#     return render(request,"result.html",{'result':res})
