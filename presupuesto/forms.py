from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.layout import Layout, Fieldset, Row, Column

class Proyeccion(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    valor = forms.IntegerField(required=True)
    duracion = forms.IntegerField(required=True)
    fecha_inicio = forms.DateField(required=True)
    ciclo_inversion = forms.IntegerField(required=True)
    t_int_esperada = forms.FloatField(required=True)
    t_int_inversion = forms.FloatField(required=True)
    precision = forms.TypedChoiceField(
        label = "Precisión",
        choices = ((0, "Baja"), (1, "Normal"), (2, "Alta"), (3, "Muy alta")),
        widget = forms.RadioSelect,
        initial = '1',
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-5 text-white h3'
        self.helper.field_class = 'col-7'
        self.helper.form_method = 'post'
        #self.helper.form_action = 'submit_survey'

        submit = Submit("submit", "Enviar")
        submit.field_classes = 'btn btn-dark float-end'

        #self.helper.add_input(submit)

        self.helper.layout = Layout(
            'nombre',
            'valor',
            'duracion',
            'fecha_inicio',
            'ciclo_inversion',
            't_int_esperada',
            't_int_inversion',
            'precision'
        )
        self.helper.layout.append(submit)
