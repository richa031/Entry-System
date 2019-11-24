# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class Record(models.Model):
    visitor = models.CharField(max_length=50)
    visitor_number = models.CharField(max_length=12)
    visitor_email = models.CharField(max_length=50)
    host = models.CharField(max_length=50)
    host_number = models.CharField(max_length=12)
    host_email = models.CharField(max_length=50)
    check_in = models.DateTimeField(default = timezone.now)
    check_out = models.DateTimeField(default=None, blank=True, null=True)

    def checkout_visitor(self):
        self.check_out = timezone.now()
        self.save()

    def __str__(self):
        return self.visitor
