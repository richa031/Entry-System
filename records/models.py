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
    checked_in = models.BooleanField(default=False)

    def check_out(self):
        self.check_out = timezone.now()
        self.checked_in = False
        self.save()


    def get_checkin_time(self):
        checkInTimeStamp = str(self.check_in.hour) + ":" + str(self.check_in.minute) + "  " + str(self.check_in.day) + "/" + str(self.check_in.month)
        return checkInTimeStamp

    def get_checkout_time(self):
        checkOutTimeStamp = str(self.check_out.hour) + ":" + str(self.check_out.minute) + "  " + str(self.check_out.day) + "/" + str(self.check_out.month)
        return checkOutTimeStamp
    def __str__(self):
        return self.visitor
