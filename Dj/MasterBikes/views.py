from django.shortcuts import render
from .models import TipoUsuario, Talla, TipoBici, FormaPago, TipoProducto,Estado,Usuario,Arriendo,Reparacion, Pago, Detalle, Despacho, Producto
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    context={}
    return render(request, 'pages/index.html', context)

def crud_usuarios(request):
    usuarios = User.objects.all()
    detalle = Usuario.objects.all()
    tipoUsuarios = TipoUsuario.objects.all()
    context={
        "usuarios" : usuarios,
        "detalle" : detalle,
        "tipoUsuarios": tipoUsuarios,
    }
    return render(request, 'pages/crud/crud_usuarios.html', context)

def crud_arriendos(request):
    arriendos = Arriendo.objects.all()
    usuarios = User.objects.all()
    detalle = Usuario.objects.all()
    talla = Talla.objects.all()
    formaPago = FormaPago.objects.all()
    tipoBici = TipoBici.objects.all()
    context={
        "usuarios" : usuarios,
        "detalle" : detalle,
        "arriendos" : arriendos,
        "talla" : talla,
        "formaPago" : formaPago,
        "tipoBici" : tipoBici
    }
    return render(request, 'pages/crud/crud_arriendos.html', context)

def crud_reparacion(request):
    reparaciones = Reparacion.objects.all()
    usuarios = User.objects.all()
    detalle = Usuario.objects.all()
    estado = Estado.objects.all()
    context={
        "reparaciones" : reparaciones,
        "usuarios" : usuarios,
        "detalle" : detalle,
        "estado" : estado,
    }
    return render(request, 'pages/crud/crud_reparacion.html', context)

def crud_ventas(request):
    pagos = Pago.objects.all()
    usuarios = User.objects.all()
    detalle = Usuario.objects.all()
    formaPago = FormaPago.objects.all()
    detallePago = Detalle.objects.all()
    productos = Producto.objects.all()
    despachos = Despacho.objects.all()
    context={
        "pagos" : pagos,
        "usuarios" : usuarios,
        "detalle" : detalle,
        "formaPago" : formaPago,
        "detallePago" : detallePago,
        "productos" : productos,
        "despachos" : despachos,
    }
    return render(request, 'pages/crud/crud_ventas.html', context)

def crud_varios(request):
    tipoUsuarios = TipoUsuario.objects.all()
    talla = Talla.objects.all()
    tipoBici = TipoBici.objects.all()
    formaPago = FormaPago.objects.all()
    tipoProducto = TipoProducto.objects.all()
    estado = Estado.objects.all()
    context = {
        "tipoUsuarios": tipoUsuarios,
        "talla" : talla,
        "tipoBici" : tipoBici,
        "formaPago" : formaPago,
        "tipoProducto" : tipoProducto,
        "estado" : estado,
    }
    return render(request, "pages/crud/crud_varios.html", context)

def Principal(request):
    context={}
    return render(request, 'pages/Principal.html', context)

def tienda(request):
    context={}
    return render(request, 'pages/tienda.html', context)