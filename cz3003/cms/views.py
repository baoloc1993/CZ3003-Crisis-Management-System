from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from cms.models import Question, CMSUser
from cms.forms import MyForm
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.utils import timezone
from cms.models import CallOperatorForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.middleware.csrf import get_token


class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


def login(request):
	dm = CMSUser(username = 'admin', user_type = 'DM')
	csrf_token = get_token(request)
	state = "Please log in below..."
	username = password = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
        	
		user = authenticate(username=username, password=password)
		

		if user is not None:
			if user.is_active:
				#check the type of user
				#cmsuser = CMSUser.objects.filter(username = username)
				if (username == 'decisionmaker'):
					formList = CallOperatorForm.objects.all()
					return render_to_response("DMindex.html", {'formList':formList})
					#return render_to_response("index.html", RequestContext(request))
				if (username == 'operator'):
					return render_to_response("index.html", RequestContext(request))	
				else:
					return render_to_response("index.html", RequestContext(request))	
				state = "You're successfully logged in!"
					
			else:
				state = "Your account is not active, please contact the site admin."
		else:
			state = "Your username and/or password were incorrect."
	return render_to_response('admin/login2.html', RequestContext(request),{'state':state, 'username': username})

def index(request):
	csrf_token = get_token(request)
	formList = CallOperatorForm.objects.all().filter(status='2')
	if request.user.is_authenticated():
		return render_to_response("index.html", {'formList':formList})
	else:
		return render_to_response("admin/login2.html", RequestContext(request) )


class IncidentListView(ListView):
    model = CallOperatorForm
    def get_context_data(self, **kwargs):
        context = super(IncidentListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class DetailView(generic.DetailView):
    model = CallOperatorForm
    template_name = 'detail.html'

class UpdateView(FormView):
    template_name = 'update.html'
    form_class = MyForm
    success_url = 'index'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(UpdateView, self).form_valid(form)



def DMindex(request):
    formList = CallOperatorForm.objects.all()
    return render_to_response("DMindex.html", {'formList':formList})

def DMUpdate(request, pk=0):
    crisis = CallOperatorForm.objects.get(id=pk)
    crisis.status = 2
    crisis.save()
    return render_to_response("DMUpdate.html")

class DMIncidentListView(ListView):
    model = CallOperatorForm
    template_name = "DMIncidentListView.html"

class DMDetailView(generic.DetailView):
    model = CallOperatorForm
    template_name = 'DMdetail.html'



def logout_view(request):
	logout(request)
	return render_to_response("admin/login2.html", RequestContext(request))


def home(request):
	csrf_token = get_token(request)
	if request.user.is_authenticated():
		return render_to_response ("index.html",RequestContext(request))
	else:
		return render_to_response("admin/login2.html", RequestContext(request))
