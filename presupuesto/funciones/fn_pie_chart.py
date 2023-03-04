import matplotlib.pyplot as plt
import io
import base64
import numpy as np
from .fn_formato import formatNumber

def func_pct(pct, allvals):
    absolute = int(round((pct/100.*np.sum(allvals)), 0))
    return "{:.1f}%\n${}".format(pct, formatNumber(absolute, 0))

def crear_pie_chart(df):
    data = [df['Valor cuota'].sum(), df['Ganancia'].sum()]
    fig, ax = plt.subplots()
    fig.set_facecolor('#efe6d4')
    ax.set_facecolor('#9cebd6')

    ax.pie(data,
        labels=['Cuotas ahorro', 'Ganancia'],
        explode=[0, 0.2],
        shadow=True,
        startangle=120,
        autopct=lambda pct: func_pct(pct, data),
        textprops={'color':"w"},
        wedgeprops={'linewidth': 3.0, 'edgecolor': 'black'}
    )

    plt.legend(loc = 'center', bbox_to_anchor = (1, 1), title = 'Presupuesto')
    #plt.legend(loc = 'best', bbox_to_anchor = (0, 1.2), title = 'Presupuesto')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', transparent=True)
    buffer.seek(0)

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return image_base64