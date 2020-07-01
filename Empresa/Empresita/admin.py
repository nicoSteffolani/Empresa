from django.contrib import admin
from Empresita.models import *

# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'rut']

class ProductoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Descripcion', {'fields':('nombre',)
        }),

        ('Variables', {'fields':('precio', 'stock',)
        }),

        ('Detalles', {'fields':('categori', 'proveedor',)
        })

    )

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'rut']

    search_fields = ['nombre', 'rut']

class VentaAdmin(admin.ModelAdmin):
    exclude = ['monto_final']

    list_display = ['produc', 'client', 'cantidad', 'fecha', 'desc', 'precio_final']


admin.site.register(Venta, VentaAdmin)
admin.site.register(Direccion,)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria,)


