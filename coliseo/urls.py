"""coliseo URL Configuration

pruebas kcadena

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app_coliseo.views import IndexView

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(),name="index"),
    url(r'^inicio$', 'app_coliseo.views.Inicio',name="inicio"),
    url(r'^base$', 'app_coliseo.views.Base',name="base"),
    url(r'^persona$', 'app_coliseo.views.Personas',name="persona"),
    url(r'^campeonato$', 'app_coliseo.views.Campeonatos',name="campeonato"),
    url(r'^equipo$', 'app_coliseo.views.Equipos',name="equipo"),
    url(r'^programacion$', 'app_coliseo.views.PartidosList',name="programacion"),
    url(r'^personasl$', 'app_coliseo.views.PersonasList',name="personasl"),
    url(r'^jugadoresl$', 'app_coliseo.views.JugadoresList',name="jugadoresl"),
    url(r'^campeonatosl$', 'app_coliseo.views.CampeonatosList',name="campeonatosl"),
    url(r'^gpl$', 'app_coliseo.views.GPList',name="gpl"),
    url(r'^equiposl$', 'app_coliseo.views.EquiposList',name="equiposl"),
    url(r'^apl$', 'app_coliseo.views.APList',name="apl"),
    url(r'^jugadores$', 'app_coliseo.views.Jugadores',name="jugadores"),
    url(r'^partidos$', 'app_coliseo.views.Partidos',name="partidos"),
    url(r'^partidoAnotacion$', 'app_coliseo.views.PartidoAnotaciones',name="partidoAnotacion"),
    url(r'^partidoArbitro$', 'app_coliseo.views.PartidoArbitros',name="partidoArbitro"),
    url(r'^administrador$', 'app_coliseo.views.Administrador',name="administrador"),    
]
