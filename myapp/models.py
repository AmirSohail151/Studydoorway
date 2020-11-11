from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Classroom(models.Model):
	name=models.CharField(max_length=30,)
	section=models.CharField(max_length=30, null=True)
	subject=models.CharField(max_length=30, null=True)
	class_key=models.CharField(max_length=30, null=True)
	date_created=models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Assignment(models.Model):
	title=models.CharField(max_length=30,null=True)
	instruction=models.CharField(max_length=30,null=True)
	points=models.IntegerField(default=0,null=True)
	date_created=models.DateTimeField(auto_now_add=True, null=True)
	upload_img=models.ImageField(upload_to='images/',blank=True,null=True)

	def __str__(self):
		return self.title


RATE_CHOICES=[
 	(1,'1-OK'),
 	(2,'2-Normal'),
 	(3,'3-Good'),
 	(4,'4-Very Good'),
 	(5,'5-Perfect'),
 ]
class Review(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	classroom=models.ForeignKey(Classroom, on_delete=models.CASCADE)
	comment=models.TextField(max_length=300,blank=True)
	rating = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

	def __str__(self):
		return self.user.username





