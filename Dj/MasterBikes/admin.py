from django.contrib import admin
from .models import Usuario, Talla, TipoBici, FormaPago, Arriendo, TipoProducto, Producto, Estado, Reparacion, Pago, Detalle, Despacho

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Talla)
admin.site.register(TipoBici)
admin.site.register(FormaPago)
admin.site.register(Arriendo)
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(Estado)
admin.site.register(Reparacion)
admin.site.register(Pago)
admin.site.register(Detalle)
admin.site.register(Despacho)