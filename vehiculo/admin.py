from django.contrib import admin

# Register your models here.

from .models import VehiculoModel

admin.site.site_header = 'Proyecto Vehículos Django'
admin.site.index_title = 'Panel de control Proyecto Django'
admin.site.site_title = 'Administrador Django'

class VehiculosAdmin(admin.ModelAdmin):
    readonly_fields = ('clasificacion', 'fecha_creacion', 'fecha_modificacion')
    list_display = ('marca', 'modelo', 'categoria', 'precio', 'clasificacion')
    search_fields = ('marca', 'modelo', 'categoria')
    ordering = ('marca',)
    list_filter = ('fecha_creacion', 'precio')

admin.site.register(VehiculoModel, VehiculosAdmin)
