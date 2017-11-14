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
    def __str__(self):
        return self.fname +" "+ self.mname +" "+ self.lname

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
        profile.save()
