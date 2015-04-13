from django.conf.urls import patterns, url

from cms import views

urlpatterns = patterns('',
		url(r'^$', views.home, name = 'home'),	
		url(r'^login$', views.login, name='login'),
		url(r'^logout/$', 'django.contrib.auth.views.logout',
				  {'next_page': '/home/login'}),
		
		url(r'^nea$', views.UpdateNEAView.as_view(), name='updateNEA'),

		url(r'^dmindex', views.DMindex, name='DMindex'),
		url(r'^dmarchive/(?P<pk>\d+)/$', views.DMDetailView.as_view(), name='DMdetail'),
		url(r'^dmterminate/(?P<pk>\d+)/$', views.DMTerminateView.as_view(), name='DMterminate'),
		url(r'^dmincidents$', views.DMIncidentListView.as_view(), name='DMincident-list'),
		url(r'^dmterminate$', views.DMTerminateListView.as_view(), name='DMterminatelist'),
		url(r'^dmoldlist$', views.DMOldListView.as_view(), name='DMoldlist'),
		url(r'^dmold/(?P<pk>\d+)/$', views.DMOldView.as_view(), name='DMold'),
		url(r'^dmupdate/(?P<pk>\d+)/$', views.DMUpdate, name='DMupdate'),
		url(r'^dmupdateterminate/(?P<pk>\d+)/$', views.DMUpdateTerminate, name='DMupdateterminate'),

		url(r'^index', views.index, name='index'),
		url(r'^emailSend', views.email, name='emailSend'),
		url(r'^updateIncident$', views.UpdateView.as_view(), name='updateIncident'),
		url(r'^updateCrisis$', views.UpdateCrisisView.as_view(), name='updateCrisis'),		
		url(r'^incidents$', views.IncidentListView.as_view(), name='incident-list'),
		url(r'^codelete/(?P<pk>\d+)/$', views.CODelete, name='codelete'),


		url(r'^archive/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
		url(r'^customerindex', views.customerindex, name='customerindex'),


		url(r'^facebook', views.facebook, name='facebook'),
		url(r'^twitter', views.twitter, name='twitter'),
)
