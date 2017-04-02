from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^request', views.request, name="request"),
	url(r'^serverStatus', views.serverStatus, name="serverStatus"),
	url(r'^kill', views.kill, name="kill"),
]