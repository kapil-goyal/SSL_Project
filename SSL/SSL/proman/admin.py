from django.contrib import admin
from .models import( UserProfile, course, department, resInt,
                edu, workExp, Project, Publication, CompletedStudent, ContinuingStudent, Book)

admin.site.register(UserProfile)
admin.site.register(course)
admin.site.register(department)
admin.site.register(resInt)
admin.site.register(edu)
admin.site.register(workExp)
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Book)
admin.site.register(CompletedStudent)
admin.site.register(ContinuingStudent)
# Register your models here.
