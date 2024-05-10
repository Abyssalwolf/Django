from django.shortcuts import render
from . models import Movie

# Create your views here.

def create(request):
    if request.POST:
        title= request.POST.get('title')
        subheading= request.POST.get('sub-heading')
        summary= request.POST.get('summary')
        movie_obj=Movie(title=title,sub=subheading,sum=summary)
        movie_obj.save()

    return render(request,'create.html')

def list(request):
    moviedata = Movie.objects.all()
    return render(request,'list.html',{'movies':moviedata})

def edit(request):
    return render(request,'edit.html')