from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^dashboard/', views.dashboard, name='dashboard'),
	url(r'^update_time/', views.update_time, name='update_time'),
]