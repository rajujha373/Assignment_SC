from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from twilio.rest import Client

from retry import retry
import logging
import sys
from datetime import datetime
from core.models import basicDetails

logger = logging.getLogger(__name__)

# file_handler = logging.FileHandler(filename='log.txt')
# stdout_handler = logging.StreamHandler(sys.stdout)
# handlers = [file_handler, stdout_handler]

# logging.basicConfig(
#     level=logging.DEBUG, 
#     format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
#     handlers=handlers
# )

account_sid = 'AC1d0312d7b8aaba0048eb1ce4b8279464'
auth_token = '1b92756fd3f4a2d74e7826e10b33aaec'

phone_number = basicDetails.objects.all()[0].phone_number
wake_up_hour = basicDetails.objects.all()[0].wake_up_time
sleep_hour = basicDetails.objects.all()[0].sleep_time

@periodic_task(run_every=(crontab(minute='*/1', hour=str(wake_up_hour) + '-'+ str(sleep_hour))), name="send_sms", ignore_result=True) #minute='*/1',
@retry(Exception, tries=4)
def send_sms():
	try:
		client = Client(account_sid, auth_token)
		message = client.messages.create(body='Hi your name is John', from_='+12527877175', to='+91'+ str(phone_number))
	except Exception as e:
		logger.error(e)
		raise Exception
		print('saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')


	print('senttttttttttt')

			
