from django.conf.urls import patterns, url

from cms import views

urlpatterns = patterns('',
	    url(r'^login$', views.login, name='login'),
	    url(r'^index$', views.index, name='index'),
)
