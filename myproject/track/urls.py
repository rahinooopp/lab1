
from django.urls import path,include

from .views import *


urlpatterns = [

    path('',alltrack),
    path('id/',gettrackbyid),
    path('insert/',inserttrack),
    path('updated/<int:id>/',updatedtrack, name='updatetrack'),
    path('deleted/<int:id>/', deletedtrack, name='deletetrack')
    

]
