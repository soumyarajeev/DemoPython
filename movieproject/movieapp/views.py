from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from . models import Movie
# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,"index.html",context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'mov':movie})
def add_movie(request):
    if request.method == "POST":
        name=request.POST.get('name')
        desc = request.POST.get('despn')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
        return redirect('/')
    return render(request,"add.html")
def update(request,mov_id):
    movie_id=Movie.objects.get(id=mov_id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie_id)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'movie':movie_id})
def delete(request,mov_id):
    if request.method == "POST":
        movie=Movie.objects.get(id=mov_id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")