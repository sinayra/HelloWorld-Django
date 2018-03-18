from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .forms import nameForm

# Create your views here.

def get_name(request):
	msg = ''
	if request.method == 'POST':
		form = nameForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			name = data['name']

			msg = "Hello " + name + "!"

	else:
		form = nameForm()

	return render(request, 'index.html', {'form': form, 'msg' : msg})
