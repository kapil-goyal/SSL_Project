from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import EditProfileForm, addCourse
from .models import course, UserProfile

def index(request):
    return render(request,'proman/home.html'
    )

def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/proman/profile/')
        else:
            return redirect('/proman/login/')
    else:
        return render(request, 'proman/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<script>alert('Registration Succesful');</script>")
        else:
            return HttpResponse("<script>alert('InvalidUser');</script>")
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'proman/login.html', args)

def view_profile(request):
    user = request.user
    first = user.first_name
    last = user.last_name
    return render(
        request,
        'proman/profile.html',
        {'user' : user}
    )

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        inst = UserProfile.objects.get(user=request.user)
        if form.is_valid():
            inst.title = form.cleaned_data['title']
            inst.fname = form.cleaned_data['fname']
            inst.mname = form.cleaned_data['mname']
            inst.lname = form.cleaned_data['lname']
            inst.email = form.cleaned_data['email']
            inst.dep = form.cleaned_data.get('dep')
            inst.save()
            return redirect('/proman/profile/')
        # else:
        #     return redirect('/proman/edit-profile/')
    else:
        form = EditProfileForm()
        return render (
            request,
            'proman/edit_profile.html',
            {'form' : form}
        )

def edit_profile_addcourse(request):
    if request.method == 'POST':
        form = addCourse(request.POST)
        instance = course.objects.create()
        if form.is_valid():
            instance.year = form.cleaned_data['year']
            instance.semester = form.cleaned_data['semester']
            instance.name = form.cleaned_data['name']
            instance.course_code = form.cleaned_data['course_code']
            instance.prof = request.user
            instance.save()
            return redirect('/proman/profile/')
    else:
        form = addCourse()
        return render (
            request,
            'proman/edit_profile.html',
            {'form' : form}
        )


