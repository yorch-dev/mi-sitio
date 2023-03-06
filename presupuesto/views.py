from django.shortcuts import render, redirect
from .funciones.fn_proyeccion_ahorro_y_dp import proyeccion_ahorro_y_dp as padp
from .funciones.fn_pie_chart import crear_pie_chart
from datetime import date
import regex as re
from .forms import Proyeccion
import pandas as pd
import numpy as np

# Create your views here.
def ahorro(request):

    if request.method == 'POST':

        form = Proyeccion(request.POST)
        if form.is_valid():
            producto =form.cleaned_data['nombre']
            valor =form.cleaned_data['valor']
            duracion = form.cleaned_data['duracion']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            ciclo_inversion = form.cleaned_data['ciclo_inversion']
            t_int_esperada = form.cleaned_data['t_int_esperada']
            t_int_inversion = form.cleaned_data['t_int_inversion']
            precision = form.cleaned_data['precision']


            if precision == 'Baja':
                precision = 0.001
            elif precision == 'Alta':
                precision = 0.00005
            elif precision == 'Muy alta':
                precision = 0.00001
            else:
                precision = 0.0001

            df, monto_objetivo, tasa_int_personal = padp(
                valor_producto = valor,
                t_vida = duracion,
                fecha_inicio = fecha_inicio,
                dias_ciclo = ciclo_inversion,
                t_int_objetivo = t_int_esperada,
                t_int_dp = t_int_inversion,
                precision = 0.001
            )

            df['Cuota invertida'] = df['Cuota invertida'].replace({True: '✔', False: '❌'})
            df['Valor cuota %'] = df['Valor cuota'] / (df['Valor cuota'] + df['Ganancia'])
            df['Ganancia %'] = df['Ganancia'] / (df['Valor cuota'] + df['Ganancia'])
            df['Acumulado'] = np.cumsum(df['Valor cuota'] + df['Ganancia'])

            df_html = df.to_html(index = False)
            clases_bstp = 'table table-responsive-md table-dark table-striped text-center'
            clean_df_html = re.sub(r'<tr.*>', '<tr>', df_html.replace('border="1" class="dataframe', f'class="{clases_bstp}'))
            
            pie_chart = crear_pie_chart(df)

            ctx = {
                'producto' : producto,
                'monto_objetivo' : monto_objetivo,
                'tasa_int_personal' : tasa_int_personal,
                'form' : form,
                'df' : clean_df_html,
                'pie' : pie_chart,
            }

            return render(request, 'proyectando-ahorro/proyectando-ahorro.html', ctx)
        else:
            form = Proyeccion()
            ctx = {
                'form' : form
            }
            return redirect('ahorro')
            
    else:
        form = Proyeccion()

        ctx = {
            'form' : form
        }

        return render(request, 'proyectando-ahorro/proyectando-ahorro.html', ctx)
