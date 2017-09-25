from __future__ import unicode_literals

from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=20)
    mentor = models.CharField(max_length=20)
    mem1 = models.CharField(max_length=20)
    mem2 = models.CharField(max_length=20)
    mem3 = models.CharField(max_length=20)
    member_nos = models.IntegerField()

    def __str__(self):
      return self.team_name

# Create your models here.
