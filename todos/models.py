from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)
    user = models.CharField(max_length=100, default='nouser')
    priority = models.IntegerField(default=0)
    description = models.CharField(default="",max_length=1000)
    duedate = models.DateField(default=timezone.now() + timedelta(1) )

    def __str__(self):
        return self.title

    @property
    def remaining_days(self):
        remaining = (self.duedate - timezone.now().date()).days
        return remaining