from django.db import models


class Activity(models.Model):
    title = models.CharField(max_length=120)
    daily_time = models.TimeField(auto_now_add=True)
    weekly_time = models.DateTimeField(auto_now_add = True)
