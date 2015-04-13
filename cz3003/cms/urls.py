from django.conf.urls import patterns, url

from cms import views

urlpatterns = patterns('',
		url(r'^$', views.home, name = 'home'),	
		url(r'^login$', views.login, name='login'),
		url(r'^logout/$', 'django.contrib.auth.views.logout',
				  {'next_page': '/home/login'}),

		url(r'^dmindex', views.DMindex, name='DMindex'),
		url(r'^dmarchive/(?P<pk>\d+)/$', views.DMDetailView.as_view(), name='DMdetail'),
		url(r'^dmincidents$', views.DMIncidentListView.as_view(), name='DMincident-list'),
		url(r'^dmupdate/(?P<pk>\d+)/$', views.DMUpdate, name='DMupdate'),

		url(r'^index', views.index, name='index'),
		# url(r'^tweeter', views.tweeter, name='tweeter'),
		url(r'^facebook', views.facebook, name='facebook'),
		url(r'^update$', views.UpdateView.as_view(), name='detail'),
		url(r'^incidents$', views.IncidentListView.as_view(), name='incident-list'),
		url(r'^archive/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)
