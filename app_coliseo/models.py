
from __future__ import unicode_literals

from django.db import models


class Campeonato(models.Model):
    id_campeonato = models.IntegerField(primary_key=True)
    nombre_campeonato = models.CharField(max_length=50, blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    id_disciplina = models.ForeignKey('Disciplina', db_column='id_disciplina')

    class Meta:
        managed = False
        db_table = 'campeonato'


class Disciplina(models.Model):
    id_disciplina = models.IntegerField(primary_key=True)
    nombre_diciplina = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplina'


class Equipo(models.Model):
    id_equipo = models.IntegerField(primary_key=True)
    nombre_equipo = models.CharField(max_length=50)
    id_campeonato = models.ForeignKey(Campeonato, db_column='id_campeonato')
    id_representante = models.ForeignKey('Persona', db_column='id_representante')

    class Meta:
        managed = False
        db_table = 'equipo'


class Jugador(models.Model):
    id_jugador = models.IntegerField(primary_key=True)
    id_equipo = models.ForeignKey(Equipo, db_column='id_equipo')
    id_persona = models.ForeignKey('Persona', db_column='id_persona')

    class Meta:
        managed = False
        db_table = 'jugador'


class Lugar(models.Model):
    id_lugar = models.IntegerField(primary_key=True)
    nombre_lugar = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    observacion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lugar'


class Partido(models.Model):
    id_partido = models.IntegerField(primary_key=True)
    id_equipo_local = models.ForeignKey(Equipo, db_column='id_equipo_local',related_name="rname1")
    id_equipo_visitante = models.ForeignKey(Equipo, db_column='id_equipo_visitante')
    fecha_partido = models.DateField(blank=True, null=True)
    id_lugar = models.ForeignKey(Lugar, db_column='id_lugar')
    planilla = models.CharField(max_length=200, blank=True, null=True)
    observacion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partido'


class PartidoAnotacion(models.Model):
    id_partido_anotacion = models.IntegerField(primary_key=True)
    id_partido = models.ForeignKey(Partido, db_column='id_partido')
    id_jugador = models.ForeignKey(Jugador, db_column='id_jugador')
    cantidad = models.IntegerField(blank=True, null=True)
    observacion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partido_anotacion'


class PartidoArbitro(models.Model):
    id_partido = models.ForeignKey(Partido, db_column='id_partido')
    id_persona = models.ForeignKey('Persona', db_column='id_persona')
    id_rol = models.ForeignKey('Rol', db_column='id_rol')

    class Meta:
        managed = False
        db_table = 'partido_arbitro'
        unique_together = (('id_partido', 'id_persona', 'id_rol'),)


class Persona(models.Model):
    id = models.IntegerField(primary_key=True)
    p_nombre = models.CharField(max_length=50, blank=True, null=True)
    o_nombre = models.CharField(max_length=50, blank=True, null=True)
    p_apellido = models.CharField(max_length=50, blank=True, null=True)
    s_apellido = models.CharField(max_length=50, blank=True, null=True)
    id_tipo_identificacion = models.ForeignKey('TipoIdentificacion', db_column='id_tipo_identificacion')
    identificacion = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    es_arbitro = models.CharField(max_length=1, blank=True, null=True)
    fotografia = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persona'


class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class TipoIdentificacion(models.Model):
    id_tipo_identificacion = models.IntegerField(primary_key=True)
    nombre_ti = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_identificacion'
