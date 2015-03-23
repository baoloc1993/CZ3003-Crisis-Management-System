from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from cms.models import Question
from cms.forms import MyForm
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.utils import timezone
from cms.models import CallOperatorForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
    formList = CallOperatorForm.objects.all()
    return render_to_response("index.html", {'formList':formList})


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
