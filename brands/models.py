# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Info(models.Model):
    owner = models.ForeignKey('auth.User', related_name='info', on_delete=models.PROTECT)
    interviewee = models.CharField(max_length=250, default='')
    longitude = models.DecimalField(max_digits=9, decimal_places=6,null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,null=True, blank=True)
    favorite = models.CharField(max_length=75, default='')
    created = models.DateTimeField(auto_now_add=True)
