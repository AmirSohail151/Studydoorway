from django import forms
from .models import Classroom
from .models import Assignment
from .models import Review,RATE_CHOICES

class ClassroomForm(forms.ModelForm):
	class Meta():
		model=Classroom
		fields="__all__"

	
class AssignmentForm(forms.ModelForm):
	class Meta():
		model=Assignment
		fields="__all__"
		
class ReviewForm(forms.ModelForm):
	rating=forms.ChoiceField(choices=RATE_CHOICES,widget=forms.Select(),required=True)
	class Meta():
		model=Review
		fields=['comment','rating']

