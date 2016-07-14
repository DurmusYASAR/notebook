from django.db import models
from django.utils import timezone
from datetime import datetime
from django import forms
from django_cron import CronJobBase, Schedule

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    creation_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField()

    def creation(self):
        self.creation_time = timezone.now()
        self.save()

    def __str__(self):
        return self.title
