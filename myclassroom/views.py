from django.shortcuts import render,redirect


# Create your views here.


def Classroomhome():
	return render(request,'myclassroom/classroombase.html')
	