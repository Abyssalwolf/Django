from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def print_hello(request):
    moviedata={
        'movies' : [
            {
            'title': 'Avesham',
            'sub':'Edamwone',
            'sum':'Fafascne aan',
            'success' : True 
        },
        {
            'title': 'Manjumel',
            'sub':'Kuttetaa',
            'sum':'Soubin scn aan',
            'success' : True 
        },
        {
            'title': 'Premalu',
            'sub':'Eyy pedikkanda... girlfriend onnum alla',
            'sum':'Mamitha scn aan',
            'success' : True 
        },
        {
            'title': 'Varshangalk shesham',
            'sub':'Pattikalee',
            'sum':'Nivin Pauly scne aan',
            'success' : False 
        },
        {
            'title': 'Malai kottu vaaliban',
            'sum':'Mohan lal scne aan',
            'success' : False 
        }
        ]
    }
    return render(request,'hello.html',moviedata)

