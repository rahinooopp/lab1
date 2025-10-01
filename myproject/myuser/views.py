from django.shortcuts import render
from django.http import HttpResponse

from myuser.views import *
# Create your views here.
def login(request):
    return HttpResponse("<h1>login page</h1>")
def logout(request):
    return HttpResponse("<h1>logout page</h1>")
def register(request):
    return HttpResponse("<h1>welcome to register page</h1>")
