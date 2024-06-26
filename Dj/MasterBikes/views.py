from django.shortcuts import render
from .models import TipoUsuario, Talla, TipoBici, FormaPago, TipoProducto,Estado
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    context={}
    return render(request, 'pages/index.html', context)

def crud_usuarios(request):
    context={}
    return render(request, 'pages/crud/crud_usuarios.html', context)

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