from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import EditProfileForm, addCourse, ImageUploadForm, eduForm, exForm
from .models import course, UserProfile, edu, workExp

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
        if(request.user.userprofile.image != ""):
            inst.image = request.user.userprofile.image
        if form.is_valid():
            inst.title = form.cleaned_data['title']
            inst.fname = form.cleaned_data['fname']
            inst.mname = form.cleaned_data['mname']
            inst.lname = form.cleaned_data['lname']
            inst.email = form.cleaned_data['email']
            inst.dep = form.cleaned_data.get('dep')
            inst.desig = form.cleaned_data['desig']
            inst.descrip = form.cleaned_data['descrip']
            inst.office = form.cleaned_data['office']
            inst.phn_no = form.cleaned_data['phn_no']
            inst.resid = form.cleaned_data['resid']
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

def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = UserProfile.objects.get(user=request.user)
            m.image = form.cleaned_data['image']
            m.save()
            return redirect('/proman/profile/')
    # return HttpResponseForbidden('allowed only via POST')

def edit_profile_addcourse(request):
    if request.method == 'POST':
        form = addCourse(request.POST)
        instance = course.objects.create()
        if form.is_valid():
            instance.startYear = form.cleaned_data['startYear']
            instance.endYear = form.cleaned_data['endYear']
            instance.semester = form.cleaned_data['semester']
            instance.name = form.cleaned_data['name']
            instance.course_code = form.cleaned_data['course_code']
            instance.user = request.user.userprofile
            instance.save()
            return redirect('/proman/profile/')
    else:
        form = addCourse()
        return render (
            request,
            'proman/edit_profile.html',
            {'form' : form}
        )

def edit_profile_addedu(request):
    if request.method == 'POST':
        form_edu = eduForm(request.POST)
        instance = edu.objects.create()
        if form_edu.is_valid():
            instance.college = form_edu.cleaned_data['college']
            instance.degree = form_edu.cleaned_data['degree']
            instance.descrip = form_edu.cleaned_data['descrip']
            instance.startTime = form_edu.cleaned_data['startTime']
            instance.endTime = form_edu.cleaned_data['endTime']
            instance.user = request.user.userprofile
            instance.save()
            return redirect('/proman/profile/')
    else:
        form_edu = eduForm()
        return render (
            request,
            'proman/edit_profile.html',
            {'form_edu' : form_edu}
        )

def edit_profile_addexp(request):
    if request.method == 'POST':
        form_edu = exForm(request.POST)
        instance = workExp.objects.create()
        if form_edu.is_valid():
            instance.desig = form_edu.cleaned_data['desig']
            instance.firm = form_edu.cleaned_data['firm']
            instance.descrip = form_edu.cleaned_data['descrip']
            instance.startTime = form_edu.cleaned_data['startTime']
            instance.endTime = form_edu.cleaned_data['endTime']
            instance.user = request.user.userprofile
            instance.save()
            return redirect('/proman/profile/')
    else:
        form_edu = exForm()
        return render (
            request,
            'proman/edit_profile.html',
            {'form_edu' : form_edu}
        )
