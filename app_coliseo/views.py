from django.shortcuts import render,render_to_response,RequestContext,redirect
from django.views.generic import TemplateView

from django.utils import timezone

from .forms import MyModel
from .forms import ModelPersona

# Create your views here.

class IndexView(TemplateView):
	template_name='index.html'

class Partidos(TemplateView):
	template_name='partidos.html';

class Equipos(TemplateView):
	template_name='equipos.html'


def Personas(request):

    if request.method == "POST":
        form = MyModelForm(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('victory')
    else:
        form = ModelPersona()

    return render(request, "form.html", {'form': form})