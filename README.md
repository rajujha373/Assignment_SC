# TO RUN.

1. Install virtualenv
	<code>pip install virtualenv</code>
2. Create a virutal environment
	<code>virtualenv venv</code>
3. Activate virtualenv
	<code>source venv/bin/activate</code>
4. Install Dependencies 
	<code>pip install -r requirements.txt</code>
5. Run localhost
	<code>python manage.py runserver</code>
6. Run Celery worker
	<code>celery -A cronNotifier worker -l info</code>
7. Run celery beat
 	<code>celery -A cronNotifier beat -l info</code>

# ALLOWED URLS

1. localhost:8000/dashboard <= shows the details about what mobile number is provided and what timings are set for sms
2. localhost:8000/update_time <= to see and update the timing for sms