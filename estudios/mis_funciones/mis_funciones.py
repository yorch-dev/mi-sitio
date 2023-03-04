import datetime as dt
from datetime import timedelta
from ..models import F_inicio

def crear_lista(qset, n_sesiones):
    lista = []
    libres = []
    fecha_qs = F_inicio.objects.all().values()[0]['fecha_inicio']
    f_inicio = dt.datetime(fecha_qs.year, fecha_qs.month, fecha_qs.day)
    delta = dt.datetime.now() - f_inicio
    hoy = dt.datetime.now()
    
    for x in range(10):
        lista.append([])
    for x in range(10):
        dia = int((delta.days + 1 + x) % 10)
        if dia == 0:
            dia = 10
        lista[dia - 1].append(hoy + timedelta(x))
        if dia in [5, 9, 10]:
            libres.append(hoy + timedelta(x))
    for x in range(10):
        for n in range(n_sesiones):
            lista[x].append("")
    for obj in qset:
        for x in obj.dias_numero.split(', '):
            lista[int(x)-1][obj.sesion] = obj.titulo
    return (sorted(lista), [x + 1 for x in range(n_sesiones)], libres)
