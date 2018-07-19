# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .models import basicDetails

from django.views.decorators.csrf import csrf_exempt

from twilio.rest import Client

account_sid = 'AC1d0312d7b8aaba0048eb1ce4b8279464'
auth_token = '1b92756fd3f4a2d74e7826e10b33aaec'

# Create your views here.

def dashboard(request):
	import subprocess
	redis_data = subprocess.check_output("redis-cli info | grep uptime_in_seconds", shell=True)
	uptime = redis_data.split(':')[1]
	uptime_in_minutes = int(uptime)/60
	uptime_in_hours = int(uptime)/3600

	context = {
		'wake_up_time': basicDetails.objects.all()[0].wake_up_time,
		'sleep_time': basicDetails.objects.all()[0].sleep_time,
		'uptime_in_minutes' : uptime_in_minutes,
		'uptime_in_hours' : uptime_in_hours,
		'phone': basicDetails.objects.all()[0].phone_number
	}

	return render(request, 'core/dashboard.html', context)
	#return HttpResponse(localhost_data)
	#return HttpResponse('The application has been running for <b>'+ str(uptime_in_minutes) + '</b> minutes. That is equivalent to <b>'+ str(uptime_in_hours) +'</b> hours')

def update_time(request):
	if request.method == 'POST':
		userDetails = basicDetails.objects.all()[0] #getting just the first and only basicDetails object that we have created in the backend manually.
		userDetails.wake_up_time = request.POST.get('wake_up_hour')
		userDetails.sleep_time = request.POST.get('sleep_hour')

		userDetails.save()

		return redirect('update_time')
	else:
		userDetails = basicDetails.objects.all()[0]
		context = {
			'wake_up_time': userDetails.wake_up_time,
			'sleep_time': userDetails.sleep_time,
		}
		return render(request, 'core/update_time.html', context)
		#return HttpResponse('update section')
