

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Trainee
from .views import *

# Create your views here.

def alltrainees(request):
    trainee=Trainee.objects.all()
   # trainee=[[1,'ahmed','ahmed@gmail.com','photo'],[2,'mo3taz','mo3taz@gmail.com','photo']]
    return render(request,'alltrainee.html', context={'trainee':trainee})
def gettraineebyid(request):
    return HttpResponse('<h1>hello trainee in this  page</h1>')
def inserttrainee(request):
    if request.method == "POST":
        name = request.POST['trname']
        email = request.POST['tremail']
        photo = request.FILES['trphoto']   
        Trainee.objects.create(name=name,email=email,photo=photo)
        
        

    return render(request,'insert.html')
def updatedtrainee(request,id):
    return HttpResponse(f'<h1>hello to new trainee with id {id}</h1>')
def deletedtrainee(request,id):
    return HttpResponse(f'<h1>this trainee With  id {id} is deleted</h1>')
