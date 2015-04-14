from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from cms.models import Question
from cms.forms import MyCrisisForm, MyIncidentForm, MyNEAForm
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.utils import timezone
from cms.models import CallOperatorForm
from cms.models import CrisisInstance
from cms.models import SensorData
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

def login(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                state = "You're successfully logged in!"
                return redirect('cms:index')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render(request, 'admin/login2.html', {'state':state, 'username': username})

def index(request):
    formList = CallOperatorForm.objects.all();
    crisisList = CrisisInstance.objects.all().filter(crisisStatus = 'Happening');
    sensorList = SensorData.objects.all();
    return render_to_response("index.html", {'formList':formList, 'crisisList':crisisList, 'sensorList':sensorList})

def email(request):
    crisisList = CrisisInstance.objects.all();
    return render_to_response("emailSend.php", {'crisisList':crisisList})

def customerindex(request):
    crisisList = CrisisInstance.objects.all().filter(crisisStatus = 'Happening');
    return render_to_response("customindex.html", {'crisisList':crisisList})

def facebook(request):
    return render_to_response("facebook.php")

def facebookSelect(request):
    return render_to_response("facebookSelect.html")

def facebookBegin(request):
    return render_to_response("facebookBegin.php")

def facebookEnd(request):
    return render_to_response("facebookEnd.php")

def facebookSituation(request):
    sensorList = SensorData.objects.all();
    return render_to_response("facebookSituation.php", {'sensorList':sensorList})

def twitter(request):
    return render_to_response("API/index.php")

class IncidentListView(ListView):
    model = CallOperatorForm
    template_name = "IncidentListView.html"

class DetailView(generic.DetailView):
    model = CallOperatorForm
    template_name = 'detail.html'

class UpdateView(FormView):
    template_name = 'update.html'
    form_class = MyIncidentForm
    success_url = 'index'
    def form_valid(self, form):
        form.save()
        return super(UpdateView, self).form_valid(form)

class UpdateNEAView(FormView):
    template_name = 'updateNEA.html'
    form_class = MyNEAForm
    success_url = 'nea'
    def form_valid(self, form):
        form.save()
        return super(UpdateNEAView, self).form_valid(form)

class UpdateCrisisView(FormView):
    template_name = 'updateCrisis.html'
    form_class = MyCrisisForm
    success_url = 'index'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(UpdateCrisisView, self).form_valid(form)

def DMindex(request):
    formList = CrisisInstance.objects.all().filter(crisisStatus = 'Happening');
    sensorList = SensorData.objects.all();
    return render_to_response("DMindex.html", {'formList':formList, 'sensorList':sensorList})

def DMUpdate(request, pk=0):
    crisis = CrisisInstance.objects.get(id=pk)
    crisis.crisisStatus = 'Happening'
    crisis.save()
    return render_to_response("DMUpdate.html");

def CODelete(request, pk=0):
    CallOperatorForm.objects.get(id=pk).delete();
    return render_to_response("CODelete.html");

def DMUpdateTerminate(request, pk=0):
    crisis = CrisisInstance.objects.get(id=pk)
    crisis.crisisStatus = 'Stopped'
    crisis.save()
    return render_to_response("DMUpdate.html");

class DMIncidentListView(ListView):
    model = CrisisInstance
    template_name = "DMIncidentListView.html"

class DMTerminateListView(ListView):
    model = CrisisInstance
    template_name = "DMTerminateListView.html"

class DMOldView(generic.DetailView):
    model = CrisisInstance
    template_name = "DMolddetail.html"

class DMOldListView(ListView):
    model = CrisisInstance
    template_name = "DMOldList.html"

class DMDetailView(generic.DetailView):
    model = CrisisInstance
    template_name = 'DMdetail.html'

class DMTerminateView(generic.DetailView):
    model = CrisisInstance
    template_name = 'DMterminate.html'

def logout_view(request):
	logout(request)
	return render_to_response("admin/login2.html")

def home(request):
	if request.user.is_authenticated():
		return render_to_response ("index.html")
	else:
		return render_to_response("admin/login2.html")
