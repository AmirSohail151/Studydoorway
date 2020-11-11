from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.models import User

def contact(request):
	return render(request,'myapp/base.html')


def showmyForm(request):
	if request.method=='POST':
		form=ClassroomForm(request.POST)
		if form.is_valid():
			form.save()
			messages.warning(request, 'class room created successfully')

	form = ClassroomForm()
	return render(request,'myapp/classroom_form.html',{'form':form})
	


def amir(request):
	formm=ReviewForm()
	if request.method=='POST':
		form=AssignmentForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.error(request, 'assignment created successfully')

	form = AssignmentForm()
	return render(request,'myapp/Assignment_form.html',{'form':form,'formm':formm})



def handleSignup(request):

	if request.method=="POST":
		username=request.POST['username']
		firstname=request.POST['firstname']
		lastname=request.POST['lastname']
		email=request.POST['email']
		pass1=request.POST['pass1']
		pass2=request.POST['pass2']

		if len(username)>10:
			messages.error(request, 'user name must be under 10 characters')
			return redirect('/')
		if pass1 != pass2:
			messages.error(request, 'passwords does not match each others ')
			return redirect('/')
		if not username.isalnum():
			messages.error(request, 'username can only contain letters and numbers')
			return redirect('/')		 
		#create the user
		myuser=User.objects.create_user(username,email,pass1)
		myuser.first_name=firstname
		myuser.last_name=lastname
		myuser.save()
		messages.info(request, "user is created successfully ")
		return redirect('/')
	else:
		return HttpResponse("Error 404")

def handleLogin(request):
	if request.method=="POST":
		loginusername=request.POST['loginusername']
		loginpassword=request.POST['loginpassword']
		user=authenticate(username=loginusername,password=loginpassword)

		if user is not None:
			login(request, user)
			messages.success(request, 'user is login successfully')
			return redirect('/')
		else:
			messages.error(request, 'invalid username or password :please try again')
			return redirect('/')
	return HttpResponse("Error 404")

def handleLogout(request):
	logout(request)
	messages.success(request, 'successfully logout !')
	return redirect('/')
	#return HttpResponse("logout")


def showclasses(request):
	var1=Classroom.objects.all()
	form=ReviewForm()
	return render(request,"myapp/myclassroom.html",{'var1':var1})		
	
def add_review(request,id):
	if request.user.is_authenticated:
		classroom=Classroom.objects.get(id=id)
		print()
		if request.method=="POST":
			form=ReviewForm(request.POST)
			if form.is_valid():
				print("form validation process")
				data=form.save(commit=False)
				data.user=request.user
				data.classroom=classroom
				data.save()
				return redirect("myapp:detail",id)
				# return render(request,"myapp/classdetail.html")
		else:
			form=ReviewForm()
			return render(request,"myapp/classdetail.html",{"form":form})
	else:
		return redirect("myapp:handleLogin")		


def detail(request,id):
	form = ReviewForm()
	classroom=Classroom.objects.get(id=id)
	reviews=Review.objects.filter(classroom=id).order_by('-comment')
	context={"classroom":classroom,"reviews":reviews,"form":form}
	return render(request,"myapp/classdetail.html",context)



def edit_review(request,classroom_id,review_id):
	if request.user.is_authenticated:
		classroom=Classroom.objects.get(id=classroom_id)
		review=Review.objects.get(classroom=classroom,id=review_id)
		if request.user==review.user:
			if request.method=="POST":
				form=ReviewForm(request.POST,instance=review)
				if form.is_valid():
					data=form.save(commit=False)
					data.save()
					return redirect("myapp:detail",classroom.id)
			else:
			    form=ReviewForm(instance=review)
			    return render(request, "myapp/editreview.html",{"form":form})
		else:
			return redirect("myapp:detail",classroom_id)
	else:
		return redirect("myapp:handleLogin")			


def delete_review(request,classroom_id,review_id):
	if request.user.is_authenticated:
		classroom=Classroom.objects.get(id=classroom_id)
		review=Review.objects.get(classroom=classroom,id=review_id)
		if request.user==review.user:
			review.delete()
		return redirect("myapp:detail",classroom_id)
	else:
		return redirect("myapp:handleLogin")		




