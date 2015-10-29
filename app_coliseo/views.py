from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView

class IndexView(TemplateView):
	template_name='index.html'

