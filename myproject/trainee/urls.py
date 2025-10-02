
from django.urls import path,include

from .views import *


urlpatterns = [

    path('',alltrainees),
    path('id/',gettraineebyid),
    path('insert/',inserttrainee),
    path('updated/<int:id>/',updatedtrainee, name='updatetrainee'),
    path('deleted/<int:id>/', deletedtrainee, name='deletetrainee')
    

]
