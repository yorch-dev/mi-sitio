from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.layout import Layout, Div, HTML, Field
from crispy_forms.bootstrap import AppendedText

class Proyeccion(forms.Form):

    nombre = forms.CharField(label="Nombre proyecto", max_length=20, required=True)
    valor = forms.CharField(required=True)
    duracion = forms.FloatField(label='Plazo en años', required=True, max_value=20)
    fecha_inicio = forms.DateField(required=True, widget=forms.TextInput(attrs={'type': 'date'} ))
    ciclo_inversion = forms.IntegerField(label='Días ciclo inversión', required=True)
    t_int_esperada = forms.CharField(label='Tasa cambio proyectada', required=True)
    t_int_inversion = forms.CharField(label='Tasa interés banco', required=True)
    precision = forms.TypedChoiceField(
        label = "Precisión",
        choices = ((0, "Baja"), (1, "Normal"), (2, "Alta"), (3, "Muy alta")),
        coerce = lambda x: int(x),
        widget = forms.RadioSelect(),
        initial = '1',
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-proyeccion-form'
        self.helper.form_class = 'form-horizontal was-validated show-loading-after-submit'
        self.helper.label_class = 'col-5 text-white small h4'
        self.helper.field_class = 'col-7 text-white small'
        self.helper.form_method = 'post'
        #self.helper.form_action = 'submit_survey'

        submit = Submit("submit", "Enviar")
        submit.field_classes = 'btn btn-dark float-end'

        #self.helper.add_input(submit)

        self.helper.layout = Layout(
            Field('nombre',
                css_class="small text-end",
                placeholder='Vacaciones',
                autocomplete='off',
                data_bs_toggle="popover",
                data_bs_trigger="hover",
                title="Producto o proyecto",
                data_bs_content='Nombre o título de tu proyecto'
            ),
            Field('valor',
                css_class="small input-moneda text-end",
                placeholder='$1.200.000',
                autocomplete='off',
                data_bs_toggle="popover",
                data_bs_trigger="hover",
                title="Valor actual",
                data_bs_content="Valor actual del producto o proyecto"
            ),
            Field('t_int_esperada',
                css_class="small text-end input-porcentaje",
                placeholder='1%',
                autocomplete='off',
                data_bs_toggle="popover",
                data_bs_trigger="hover",
                title="Tasa interés",
                data_bs_content="Variación futura esperada mensual"
            ),
            Field('duracion',
                css_class="small text-end",
                placeholder='1',
                autocomplete='off',
                data_bs_toggle="popover",
                data_bs_trigger="hover",
                title="Duración del proyecto",
                data_bs_content="Horizonte en años del proyecto"
            ),
            Field('fecha_inicio',
                css_class="small text-end",
                data_bs_toggle="popover",
                data_bs_trigger="hover",
                title="Fecha inicio",
                data_bs_content="Día del primer depósito a plazo"
            ),
            Field(
                'ciclo_inversion',
                css_class="small text-end",
                placeholder='60',
                autocomplete='off',
                data_bs_toggle="popover",
                data_bs_trigger="hover",
                title="Duración en días del ciclo de inversión",
                data_bs_content="Duración del ciclo en días, de los depósitos a plazo"
            ),
            Field('t_int_inversion',
                css_class="small text-end input-porcentaje",
                placeholder='0.7%',
                autocomplete='off',
                data_bs_toggle="popover",
                data_bs_trigger="hover",
                title="Tasa interés depósito a plazo",
                data_bs_content="Interés mensual del depósito a plazo"
            ),
            'precision',
            # Field('precision',
            #     data_bs_toggle="popover",
            #     data_bs_trigger="hover",
            #     title="Precisión del cálculo opcional",
            #     data_html="true",
            #     data_bs_content='En plazos extensos afecta al tiempo de respuesta. Una mayor precisión, entrega un resultado más ajustado a lo buscado.<br>(Se recomienda usa "Alta" y "Muy alta", solamente para afinar el presupuesto final)'
            # ),
            Div(submit, css_class='d-grid'),
        )
        #self.helper.layout.append(submit)
