from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
# from django.forms import NameForm

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    # elif request.method == 'POST':
        # form = NameForm(request.POST)
        # if form.is_valid():
            # return HttpResponseRedirect('/')


# Create your views here.

