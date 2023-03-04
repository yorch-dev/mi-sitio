from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column

class Proyeccion(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    valor = forms.IntegerField(required=True)
    duracion = forms.IntegerField(required=True)
    fecha_inicio = forms.DateField(required=True)
    ciclo_inversion = forms.IntegerField(required=True)
    t_int_esperada = forms.FloatField(required=True)
    t_int_inversion = forms.FloatField(required=True)
    precision = forms.CharField(max_length=20, required=False)
