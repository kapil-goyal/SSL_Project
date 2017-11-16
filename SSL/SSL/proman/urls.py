from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import(login, logout)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.my_login , name='login'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^edit-profile/$',views.edit_profile, name='edit_profile'),
    url(r'^edit-profile-upic/$',views.upload_pic, name='upload_pic'),
    url(r'^edit-profile-ac/$',views.edit_profile_addcourse, name='add_course'),
    url(r'^edit-profile-ae/$',views.edit_profile_addedu, name='add_edu'),
    url(r'^edit-profile-ax/$', views.edit_profile_addexp, name='add_exp'),
    url(r'^logout/$', logout, {'template_name': 'proman/login.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),

]