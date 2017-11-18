from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import(login, logout)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.vdep, name='view_dep'),
    url(r'^(?P<pk1>[0-9]+)/(?P<pk2>[0-9]+)/$', views.vprof, name='view_prof'),
    url(r'^login/$', views.my_login , name='login'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^edit-profile/$',views.edit_profile, name='edit_profile'),
    url(r'^edit-profile-upic/$',views.upload_pic, name='upload_pic'),
    url(r'^edit-profile-ac/$',views.edit_profile_addcourse, name='add_course'),
    url(r'^edit-profile-ae/$',views.edit_profile_addedu, name='add_edu'),
    url(r'^edit-profile-ax/$', views.edit_profile_addexp, name='add_exp'),
    url(r'^edit-profile-ai/$', views.edit_profile_addInt, name='add_Int'),
    url(r'^edit-profile-ap/$', views.edit_profile_addPro, name='add_pro'),
    url(r'^edit-profile-ab/$', views.edit_profile_addBook, name='add_book'),
    url(r'^edit-profile-apub/$', views.edit_profile_addPub, name='add_pub'),
    url(r'^edit-profile-acon/$', views.edit_profile_addCons, name='add_cons'),
    url(r'^edit-profile-acom/$', views.edit_profile_addComs, name='add_coms'),
    url(r'^logout/$', logout, {'template_name': 'proman/login.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),

]