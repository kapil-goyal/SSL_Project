from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver


class course(models.Model):
    year = models.IntegerField(default=2017)
    semester = models.CharField(max_length=4, blank=True)
    name = models.CharField(max_length=200, blank=True)
    course_code = models.CharField(max_length=6, blank=True)
    prof = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.course_code + " " + self.name


class department(models.Model):
    dep_name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.dep_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10, default='Pr.')
    fname = models.CharField(max_length=200, blank=True)
    mname = models.CharField(max_length=200, blank=True)
    lname = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    dep = models.ForeignKey(department, on_delete=models.CASCADE, null=True)
    desig = models.CharField(max_length=200, blank=True)
    descrip = models.TextField(blank=True)
    office = models.CharField(max_length=50, blank=True)
    phn_no = models.IntegerField(default=0)
    resid = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.fname + " " + self.mname + " " + self.lname


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
        profile.save()


class Projects(models.Model):
    title = models.CharField(max_length=200, blank=True)
    PI = models.CharField(max_length=200, blank=True)
    FundingAgency = models.CharField(max_length=200, blank=True)
    syear = models.IntegerField(blank=True, default=2017)
    fyear = models.IntegerField(blank=True, default=2018)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)


class Publication(models.Model):
    description = models.CharField(max_length=500, blank=True)
    books = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)


class ContinuingStudents(models.Model):
    name = models.CharField(max_length=200, blank=True)
    degree = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)


class CompletedStudent(models.Model):
    name = models.CharField(max_length=200, blank=True)
    degree = models.CharField(max_length=200, blank=True)
    supervisor = models.CharField(max_length=200, blank=True)
    thesisTitle = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
