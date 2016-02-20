from django.contrib import admin
from .models import *

# Register your models here.
class Materias_facultad(admin.ModelAdmin):
    list_display = ('nombre', 'carrera', 'anio', 'cuatrimestre')
    ordering = ('nombre',)
    search_fields = ('nombre',)


admin.site.register(Materias, Materias_facultad)
