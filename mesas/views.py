import datetime
import random
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from .models import Materias
from django.shortcuts import render, get_object_or_404

# Create your views here.
def principal(request):
    ahora = datetime.datetime.now()
    materias = Materias.objects.all()
    aleatorio = []
    for i in range(1,5):
        numeros = (random.randrange(10))
        if not numeros in aleatorio and numeros > 0:
            aleatorio.append(numeros)
    return render(request, "index.html", {'materias': materias, 'ahora':ahora, 'aleatorio':aleatorio})

def buscar(request):
    errors = []
    if 'mat' in request.GET:
        mat = request.GET['mat']
        if not mat:
            errors.append('Por favor introduce un termino de busqueda.')
        else:
            materias = Materias.objects.filter(nombre__icontains=mat)
            return render(request, 'resultado_busqueda.html',{'materias': materias, 'query': mat})

    return render(request, 'index.html', {'errors': errors})

def mostrar_materias(request, pk):
    mat = get_object_or_404(Materias, pk=pk)
    return render(request, 'detalle_materia.html', {'materias': mat})
