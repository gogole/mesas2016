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
        numeros = (random.randrange(5))
        if not numeros in aleatorio and numeros > 0:
            aleatorio.append(numeros)
    return render(request, "index.html", {'materias': materias, 'ahora':ahora, 'aleatorio':aleatorio})
