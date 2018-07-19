# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class basicDetails(models.Model):
	phone_number = models.BigIntegerField()
	wake_up_time = models.IntegerField()
	sleep_time = models.IntegerField()

	def __str__(self):
		return str(self.phone_number)