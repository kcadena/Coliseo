from django.contrib import admin

from app_coliseo.models import Campeonato, Disciplina, Equipo, Jugador, Lugar, Partido, PartidoAnotacion, PartidoArbitro, Persona, Rol, TipoIdentificacion
# Register your models here.

admin.site.register(Campeonato)
admin.site.register(Disciplina)
admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Lugar)
admin.site.register(Partido)
admin.site.register(PartidoAnotacion)
admin.site.register(PartidoArbitro)
admin.site.register(Persona)
admin.site.register(Rol)
admin.site.register(TipoIdentificacion)