from django.contrib import admin
from .models import UserProfile, course, department

admin.site.register(UserProfile)
admin.site.register(course)
admin.site.register(department)
# Register your models here.
