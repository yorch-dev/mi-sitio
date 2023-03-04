from django.shortcuts import render
from .models import Tema
from .mis_funciones.mis_funciones import crear_lista
import datetime as dt
from django.contrib.auth.decorators import login_required

@login_required()
def estudios(request):
    mis_temas = Tema.objects.all()
    try:
        sesiones = max([x[0] for x in Tema.objects.values_list('sesion')])
        temas_por_dia, n_sesiones, libres = crear_lista(mis_temas, sesiones)
    except:
        temas_por_dia = []
        n_sesiones = 0
        libres = []
    
    context = {
        'hoy' : dt.datetime.now(),
        'temas_por_dia' : temas_por_dia,
        'n_sesiones' : n_sesiones,
        'libres' : libres
    }
    
    return render(request, 'estudios/cal_estudios.html', context)
