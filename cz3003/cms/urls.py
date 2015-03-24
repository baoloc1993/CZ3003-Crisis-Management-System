from django.conf.urls import patterns, url

from cms import views

urlpatterns = patterns('',
	    url(r'^login$', views.login, name='login'),
	    url(r'^index', views.index, name='index'),
	    url(r'^update$', views.UpdateView.as_view(), name='detail'),
	    url(r'^incidents$', views.IncidentListView.as_view(), name='incident-list'),
            url(r'^archive/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)
