# mi-sitio/portfolio http://jltmdev.pythonanywhere.com

## Proyecto/Portfolio en Django

* Trabajo inicialmente en la autenticación, con accesos en el menú según se está logeado o no y si es staff para acceso administrativo.
* Incluyo correo, para trabajo de recuperación de contraseña.
* Librerías utilizadas
  * Python
    * Pandas
    * Numpy
    * Matplotlib
  * Django
    * whitenoise
    * django-crispy-forms
  * CSS - Javascript - HTML
    * Bootstrap

### Apps
 #### Incluyo 2 apps:
1. App de calendario. Es un calendario de estudios con ciclo de 10 días que muestra cada día la sesión de estudios correspondiente y el calendario futuro.
  Se gestiona modificando temas de estudio en el panel de administración, al ser parte de un modelo con datos persistentes.
2. Sistema de proyección de ahorro con inversión. Es un sistema que proyecta la inversión de las cuotas de ahorro para un proyecto a un plazo determinado.
  Se considera un aumento en el valor del proyecto dada una tasa de interés, y ese aumento se reduce con las ganancias de las cuotas invertidas en depósitos a plazo.
