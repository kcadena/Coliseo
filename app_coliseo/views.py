from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
	template_name='index.html'

class Partidos(TemplateView):
	template_name='partidos.html';

class Equipos(TemplateView):
	template_name='equipos.html'