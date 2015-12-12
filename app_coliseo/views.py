from django.shortcuts import render,render_to_response,RequestContext,redirect
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from django.utils import timezone
from app_coliseo.models import Partido, Disciplina, Campeonato, Equipo, Jugador, Lugar, PartidoAnotacion, PartidoArbitro, Persona 


from .forms import MyModel
from .forms import ModelPersona,ModelCampeonato,ModelEquipo,ModelJugador,ModelPartido,ModelPartidoAnotacion,ModelPartidoArbitro

# Create your views here.

class IndexView(TemplateView):
	template_name='inicio.html'

def Inicio(request):
    return render(request, "inicio.html")

def Base(request):
    return render(request, "base.html")

def PartidosList(request):
    partidos = Partido.objects.all()
    return render_to_response("listadoPartidos.html", dict(partidos=partidos))

def PersonasList(request):
    personas = Persona.objects.all()
    return render_to_response("listadoPersonas.html", dict(personas=personas))

def JugadoresList(request):
    jugadores = Jugador.objects.all()
    return render_to_response("listadoJugadores.html", dict(jugadores=jugadores))

def CampeonatosList(request):
    campeonatos = Campeonato.objects.all()
    return render_to_response("listadoCampeonatos.html", dict(campeonatos=campeonatos))

def GPList(request):
    gps = PartidoAnotacion.objects.all()
    return render_to_response("listadoGP.html", dict(gps=gps))     

def EquiposList(request):
    equipos = Equipo.objects.all()
    return render_to_response("listadoEquipos.html", dict(equipos=equipos))     

def APList(request):
    aps = PartidoArbitro.objects.all()
    return render_to_response("listadoAP.html", dict(aps=aps))                        

def Personas(request):

    if request.method == "POST":
        form = ModelPersona(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect("personas")
            
    else:
        form = ModelPersona()

    return render(request, "fPersona.html", {'form': form})

def Campeonatos(request):

    if request.method == "POST":
        form = ModelCampeonato(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect("campeonatos")
    else:
        form = ModelCampeonato()

    return render(request, "fCampeonato.html", {'form': form})

def Equipos(request):

    if request.method == "POST":
        form = ModelEquipo(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect("equipos")
    else:
        form = ModelEquipo()

    return render(request, "fEquipos.html", {'form': form})

def Jugadores(request):

    if request.method == "POST":
        form = ModelJugador(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect("jugadores")
            
    else:
        form = ModelJugador()

    return render(request, "fjugador.html", {'form': form})

def Partidos(request):

    if request.method == "POST":
        form = ModelPartido(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect("partidos")
            
    else:
        form = ModelPartido()

    return render(request, "fPartidos.html", {'form': form})

def PartidoAnotaciones(request):

    if request.method == "POST":
        form = ModelPartidoAnotacion(request.POST)
        if form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect("partidos_anotaciones")
            
    else:
        form = ModelPartidoAnotacion()

    return render(request, "fPartidoAnotacion.html", {'form': form})

def PartidoArbitros(request):

    if request.method == "POSTS":
        form = ModelPartidoArbitro(request.POST)
        if form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect("partidos_arbitros")            
    else:
        form = ModelPartidoArbitro()
    return render(request, "fArbitroPartido.html", {'form': form})

def Administrador(request):

    if request.method == "POST":
        form = ModelPersona(request.POST)
        if form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect("personas")
            
    else:
        form = ModelPersona()

    return render(request, "fadmin.html", {'form': form})
