from django.contrib import admin
from estudios.models import Tema, F_inicio

# Register your models here.

class TemaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'sesion', 'dias_numero')
    search_fields = ('titulo', 'sesion', 'dias_numero')

admin.site.register(Tema, TemaAdmin)

class F_inicioAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        count = F_inicio.objects.all().count()
        if count == 0:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return True

admin.site.register(F_inicio, F_inicioAdmin)