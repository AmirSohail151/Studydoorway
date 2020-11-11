from django.contrib import admin
from django.urls import path
from myclassroom import views 
from django.conf import settings
from django.conf.urls.static import static
from .import views



urlpatterns = [
   path('myclass/',views.Classroomhome,name='Classroomhome'),
 
]