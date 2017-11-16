from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile , course, department

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

class EditProfileForm(forms.Form):
    title = forms.CharField(max_length=10)
    fname = forms.CharField(max_length=200)
    mname = forms.CharField(max_length=200)
    lname = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    dep = forms.ModelChoiceField(queryset=department.objects.all())
    desig = forms.CharField(max_length=200)
    descrip = forms.CharField(max_length=500,widget=forms.Textarea)
    office = forms.CharField(max_length=50)
    phn_no = forms.IntegerField()
    resid = forms.CharField(max_length=200)

class addCourse(forms.Form):
    startYear = forms.IntegerField()
    endYear = forms.IntegerField()
    semester = forms.CharField(max_length=4)
    name = forms.CharField(max_length=200)
    course_code = forms.CharField(max_length=6)

class eduForm(forms.Form):
    college = forms.CharField(max_length=200)
    degree = forms.CharField(max_length=50)
    descrip = forms.CharField(max_length=200,widget=forms.Textarea)
    startTime = forms.CharField(max_length=50)
    endTime = forms.CharField(max_length=50)

class exForm(forms.Form):
    desig =forms.CharField(max_length=200)
    firm = forms.CharField(max_length=200)
    descrip = forms.CharField(max_length=200,widget=forms.Textarea)
    startTime = forms.CharField(max_length=50)
    endTime = forms.CharField(max_length=50)




