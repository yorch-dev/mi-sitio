from django.shortcuts import render, redirect
from .funciones.fn_proyeccion_ahorro_y_dp import proyeccion_ahorro_y_dp as padp
from .funciones.fn_formato import formatNumber
from .funciones.fn_pie_chart import crear_pie_chart
from datetime import datetime
import regex as re
from .forms import Proyeccion
import pandas as pd
import numpy as np
from .funciones.fn_str_to_number import str_to_int, str_to_percent, float_to_percent
from django.contrib.auth.decorators import login_required

@login_required()
def ahorro(request):

    if request.method == 'POST':

        form = Proyeccion(request.POST)
        if form.is_valid():
            producto = form.cleaned_data['nombre']
            valor = str_to_int(form.cleaned_data['valor'])
            duracion = form.cleaned_data['duracion']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            ciclo_inversion = form.cleaned_data['ciclo_inversion']
            t_int_esperada = str_to_percent(form.cleaned_data['t_int_esperada'])
            t_int_inversion = str_to_percent(form.cleaned_data['t_int_inversion'])
            precision = form.cleaned_data['precision']


            if precision == 0:
                precision_f = 0.001
            elif precision == 2:
                precision_f = 0.00005
            elif precision == 3:
                precision_f = 0.00001
            else:
                precision_f = 0.0001

            df, monto_objetivo, tasa_int_personal = padp(
                valor_producto = valor,
                t_vida = duracion,
                fecha_inicio = fecha_inicio,
                dias_ciclo = ciclo_inversion,
                t_int_objetivo = t_int_esperada,
                t_int_dp = t_int_inversion,
                precision = precision_f
            )


            df['Cuota invertida'] = df['Cuota invertida'].replace({True: '✔', False: '❌'})
            df['Valor cuota %'] = df['Valor cuota'] / (df['Valor cuota'] + df['Ganancia'])
            df['Ganancia %'] = df['Ganancia'] / (df['Valor cuota'] + df['Ganancia'])
            df['Acumulado'] = np.cumsum(df['Valor cuota'] + df['Ganancia'])
            
            monto_total = df['Acumulado'].iloc[-1]
            total_ahorro = df['Valor cuota'].sum()
            total_ganancia = df['Ganancia'].sum()
            saldo = monto_total - monto_objetivo
            pie_chart = crear_pie_chart(df)
            

            df['Valor cuota'] = np.array(list(map(lambda x: f'${formatNumber(x, 0)}', df['Valor cuota'])))
            df['Ganancia'] = np.array(list(map(lambda x: f'${formatNumber(x, 0)}', df['Ganancia'])))
            df['Acumulado'] = np.array(list(map(lambda x: f'${formatNumber(x, 0)}', df['Acumulado'])))
            df['Valor cuota %'] = np.array(list(map(lambda x: float_to_percent(x), df['Valor cuota %'])))
            df['Ganancia %'] = np.array(list(map(lambda x: float_to_percent(x), df['Ganancia %'])))
            df['Fecha'] = np.array(list(map(lambda x: datetime.strftime(x, '%d-%m-%Y'), df['Fecha'])))

            df_html = df.to_html(index = False)
            clases_bstp = 'table table-dark table-striped text-center'
            clean_df_html = re.sub(r'<tr.*>', '<tr>', df_html.replace('border="1" class="dataframe', f'class="{clases_bstp}'))
            
            ctx = {
                'producto' : producto,
                'monto_objetivo' :  f'${formatNumber(int(monto_objetivo), 0)}',
                'tasa_int_personal' : f'{round(tasa_int_personal * 100, 2)}%',
                'monto_total' : f'${formatNumber(int(monto_total), 0)}',
                'total_ahorro' : f'${formatNumber(int(total_ahorro), 0)}',
                'total_ganancia' : f'${formatNumber(int(total_ganancia), 0)}',
                'saldo' : f'${formatNumber(int(saldo), 0)}',
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
