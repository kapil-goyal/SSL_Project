from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile , course, department

class EditProfileForm(forms.Form):
    title = forms.CharField(max_length=10)
    fname = forms.CharField(max_length=200)
    mname = forms.CharField(max_length=200)
    lname = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    dep = forms.ModelChoiceField(queryset=department.objects.all())

class addCourse(forms.Form):
    year = forms.IntegerField()
    semester = forms.CharField(max_length=4)
    name = forms.CharField(max_length=200)
    course_code = forms.CharField(max_length=6)
   # class Meta:
   #     model = course
   #     fields = (
   #         'year',
   #         'semester',
   #         'name',
   #         'course_code',
   #        )

   # def corr_data(self):
   #     Course = course.objects.create()
   #     Course.year = self.cleaned_data['year']
   #     Course.semester = self.cleaned_data['semester']
   #     Course.name = self.cleaned_data['name']
   #     Course.course_code = self.cleaned_data['course_code']
   #
   #     return Course





