from django.shortcuts import render
from django.http import HttpResponse

from .views import *

# Create your views here.

def alltrack(request):
    tracks=[[1,'python'],[2,'java'],[3,'c#']]
    return render(request,'list.html', context={'tracks':tracks})
def gettrackbyid(request):
    return HttpResponse('<h1>hello in this track page</h1>')
def inserttrack(request):
    return HttpResponse('<h1>hello in all track page</h1>')
def updatedtrack(request,id):
    return HttpResponse(f'<h1>hello in this new track with id {id}</h1>')
def deletedtrack(request,id):
    return HttpResponse(f'<h1>this track With  id {id} is deleted</h1>')