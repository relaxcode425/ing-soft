from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TipoUsuario, Talla, TipoBici, FormaPago, TipoProducto,Estado,Usuario,Arriendo,Reparacion, Pago, Detalle, Despacho, Producto
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import TipoUsuarioForm, TallaForm,BiciForm,FormaPagoForm,TipoProductoForm,EstadoForm

# Create your views here.

""" --------------------------------------------------------------------------- """
def crud_usuarios(request):
    usuarios = User.objects.all()
    detalle = Usuario.objects.all()
    tipoUsuarios = TipoUsuario.objects.all()
    context={
        "usuarios" : usuarios,
        "detalle" : detalle,
        "tipoUsuarios": tipoUsuarios,
    }
    return render(request, 'pages/despliegue/crud_usuarios.html', context)

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
    return render(request, 'pages/despliegue/crud_arriendos.html', context)

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
    return render(request, 'pages/despliegue/crud_reparacion.html', context)

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
    return render(request, 'pages/despliegue/crud_ventas.html', context)

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
    return render(request, "pages/despliegue/crud_varios.html", context)
""" --------------------------------------------------------------------------- """

def Principal(request):
    context={}
    return render(request, 'pages/Principal.html', context)

def tienda(request):
    context={}
    return render(request, 'pages/tienda.html', context)

""" --------------------------------------------------------------------------- """

def add_tipoUsuario(request):
    form = TipoUsuarioForm()
    if request.method=="POST":
        nuevo = TipoUsuarioForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context={
                "mensaje":"Agregado con exito",
                "form":form
            }
            return render(request,"pages/agregar/add_tipoUser.html",context)
    else:
        context = {
            "form":form
        }
        return render(request,"pages/agregar/add_TipoUser.html",context)

def add_talla(request):
    form = TallaForm()
    if request.method=="POST":
        nuevo = TallaForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context={
                "mensaje":"Agregado con exito",
                "form":form
            }
            return render(request,"pages/agregar/add_talla.html",context)
    else:
        context = {
            "form":form
        }
        return render(request,"pages/agregar/add_talla.html",context)

def add_bici(request):
    form = BiciForm()
    if request.method=="POST":
        nuevo = BiciForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context={
                "mensaje":"Agregado con exito",
                "form":form
            }
            return render(request,"pages/agregar/add_TipoBici.html",context)
    else:
        context = {
            "form":form
        }
        return render(request,"pages/agregar/add_TipoBici.html",context)

def add_forma_pago(request):
    form = FormaPagoForm()
    if request.method=="POST":
        nuevo = FormaPagoForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context={
                "mensaje":"Agregado con exito",
                "form":form
            }
            return render(request,"pages/agregar/add_formaPago.html",context)
    else:
        context = {
            "form":form
        }
        return render(request,"pages/agregar/add_formaPago.html",context)

def add_tipo_producto(request):
    form = TipoProductoForm()
    if request.method=="POST":
        nuevo = TipoProductoForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context={
                "mensaje":"Agregado con exito",
                "form":form
            }
            return render(request,"pages/agregar/add_tipoProducto.html",context)
    else:
        context = {
            "form":form
        }
        return render(request,"pages/agregar/add_tipoProducto.html",context)

def add_estado(request):
    form = EstadoForm()
    if request.method=="POST":
        nuevo = EstadoForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context={
                "mensaje":"Agregado con exito",
                "form":form
            }
            return render(request,"pages/agregar/add_estado.html",context)
    else:
        context = {
            "form":form
        }
        return render(request,"pages/agregar/add_estado.html",context)


""" def genero_del(request,pk):
    try:
        genero = Genero.objects.get(id_genero=pk)
        genero.delete()

        generos = Genero.objects.all()
        context={
            "mensaje":"Registro eliminado exitosamente",
            "generos":generos
        }
        return render(request,"pages/crud_genero.html",context)
    except:
        generos = Genero.objects.all()
        context={
            "mensaje":"Error, Genero no encontrado...",
            "generos":generos
        }
        return render(request,"pages/crud_genero.html",context)

def genero_edit(request,pk):
    if pk!="":
        genero = Genero.objects.get(id_genero=pk)
        form = GeneroForm(instance=genero)
        if request.method=="POST":
            nuevo = GeneroForm(request.POST,instance=genero)

            if nuevo.is_valid():
                nuevo.save()

                context ={
                    "mensaje":"Modificado con exito",
                    "form":nuevo
                }
                return render(request,"pages/genero_edit.html",context)
        else:
            context={
                "form":form,
            }
            return render(request,"pages/genero_edit.html",context)
    else:
        generos = Genero.objects.all()
        context={
            "mensaje":"Error, genero no encontrado",
            "generos":generos
        }
        return render(request,"pages/crud_genero.html",context) """

def edit_tipoUser(request,pk):

    try:
        tipoUsuarios=TipoUsuario.objects.get(id_tipo_usuario=pk)
        context={}
        if tipoUsuarios:
            print("Se encontró el tipo de usuario")
            if request.method=="POST":
                print("es POST")
                form = TipoUsuarioForm(request.POST, instance=tipoUsuarios)
                form.save()
                mensaje="Se actualizó el tipo de usuario"
                print(mensaje)
                context={'tipoUsuarios':tipoUsuarios, 'form': form, 'mensaje': mensaje}
                return render(request, "pages/editar/edit_tipoUser.html", context)
            else:
                #no es POST
                print("No es POST")
                form = TipoUsuarioForm(instance=tipoUsuarios)
                mensaje=""
                context={'tipoUsuarios':tipoUsuarios, 'form': form, 'mensaje': mensaje}
                return render(request, "pages/editar/edit_tipoUser.html", context)
    except:
        print("Error, id no existe")
        tipoUsuarios = TipoUsuario.objects.all()
        mensaje="id no existe"
        context={'mensaje': mensaje, 'tipoUsuarios': tipoUsuarios}
        return render(request, "pages/despliegue/crud_varios.html", context)