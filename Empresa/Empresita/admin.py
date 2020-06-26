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




admin.site.register(Direccion,)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proveedor,)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria,)
admin.site.register(Venta,)

