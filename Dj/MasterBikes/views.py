from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import TipoUsuarioForm, TallaForm, BiciForm, FormaPagoForm, TipoProductoForm, EstadoForm, UsuarioForm
from .models import TipoUsuario, Talla, TipoBici, FormaPago, TipoProducto, Estado, Usuario, Arriendo, Reparacion, Pago, Detalle, Despacho, Producto

# Create your views here.
""" --------------------------------------------------------------------------- """
def imagen(request,nm):
    return
""" --------------------------------------------------------------------------- """
@login_required
def crud_usuarios(request):
    usuarios = Usuario.objects.all()
    tipoUsuarios = TipoUsuario.objects.all()
    context={
        "usuarios" : usuarios,
        "tipoUsuarios": tipoUsuarios,
    }
    return render(request, 'pages/despliegue/crud_usuarios.html', context)
@login_required
def crud_productos(request):
    productos = Producto.objects.all()
    tipoProductos = TipoProducto.objects.all()
    context={
        "productos" : productos,
        "tipoProductos" : tipoProductos,
    }
    return render(request, 'pages/despliegue/crud_productos.html', context)
@login_required
def crud_arriendos(request):
    arriendos = Arriendo.objects.all()
    usuarios = Usuario.objects.all()
    talla = Talla.objects.all()
    formaPago = FormaPago.objects.all()
    tipoBici = TipoBici.objects.all()
    context={
        "usuarios" : usuarios,
        "arriendos" : arriendos,
        "talla" : talla,
        "formaPago" : formaPago,
        "tipoBici" : tipoBici
    }
    return render(request, 'pages/despliegue/crud_arriendos.html', context)
@login_required
def crud_reparacion(request):
    reparaciones = Reparacion.objects.all()
    usuarios = Usuario.objects.all()
    estado = Estado.objects.all()
    context={
        "reparaciones" : reparaciones,
        "usuarios" : usuarios,
        "estado" : estado,
    }
    return render(request, 'pages/despliegue/crud_reparacion.html', context)
@login_required
def crud_ventas(request):
    pagos = Pago.objects.all()
    usuarios = Usuario.objects.all()
    formaPago = FormaPago.objects.all()
    detallePago = Detalle.objects.all()
    productos = Producto.objects.all()
    despachos = Despacho.objects.all()
    context={
        "pagos" : pagos,
        "usuarios" : usuarios,
        "formaPago" : formaPago,
        "detallePago" : detallePago,
        "productos" : productos,
        "despachos" : despachos,
    }
    return render(request, 'pages/despliegue/crud_ventas.html', context)
@login_required
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
@login_required
def arriendo(request):
    context={}
    return render(request, 'pages/Arriendo.html', context)
@login_required
def Mantencion(request):
    context={}
    return render(request, 'pages/Mantencion.html', context)

def Nosotros(request):
    context={}
    return render(request, 'pages/Nosotros.html', context)

def Registro(request):
    context={}
    return render(request, 'pages/Registro.html', context)

def registrar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        rut = request.POST.get('rut')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        id_tipo_usuario = TipoUsuario.objects.get(tipo='Cliente')

        # Validar y guardar los datos en la base de datos
        if username and rut and first_name and last_name and email and password and id_tipo_usuario:
            user = User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            user.set_password(password)  # Set the password using set_password
            user.save()  # Save the user instance

            usuario = Usuario(
                rut=rut,
                id_tipo_usuario=id_tipo_usuario,
                user=user  # Associate the Usuario with the User
            )
            usuario.save()  # Save the usuario instance

            return redirect('Principal')
    else:
        return render(request, 'registro.html')
def Tienda(request):
    context={}
    return render(request, 'pages/Tienda.html', context)
""" --------------------------------------------------------------------------- """
@login_required
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
            return render(request,"pages/agregar/varios/add_tipoUser.html",context)
    else:
        context = {
            "form":form
        }
        return render(request,"pages/agregar/varios/add_TipoUser.html",context)
@login_required
def del_tipoUsuario(request, pk):
    try:
        tipoUsuario = TipoUsuario.objects.get(id_tipo_usuario=pk)
        tipoUsuario.delete()

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
            "mensaje": "Registro Eliminado",
        }
        return render(request, "pages/crud-varios.html", context)
    except:
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
            "mensaje": "Error,Tipo de usuario no encontrado...",
        }
        return render(request, "pages/crud-varios.html", context)
@login_required
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
            return render(request,"pages/agregar/varios/add_talla.html",context)
    else:
        context = {
            "form":form
        }
        return render(request,"pages/agregar/varios/add_talla.html",context)
def del_talla(request, pk):
    try:
        talla = Talla.objects.get(id_talla=pk)
        talla.delete()

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
            "mensaje": "Registro Eliminado",
        }
        return render(request, "pages/despliegue/crud_varios.html", context)
    except:
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
            "mensaje": "Error,Talla no encontrada...",
        }
        return render(request, "pages/despliegue/crud_varios.html", context)
    
@login_required
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
            return render(request,"pages/agregar/varios/add_TipoBici.html",context)
    else:
        context = {
            "form":form
        }
        return render(request,"pages/agregar/varios/add_TipoBici.html",context)
@login_required
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
            return render(request,"pages/agregar/varios/add_formaPago.html",context)
    else:
        context = {
            "form":form
        }
        return render(request,"pages/agregar/varios/add_formaPago.html",context)
@login_required
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
            return render(request,"pages/agregar/varios/add_tipoProducto.html",context)
    else:
        context = {
            "form":form
        }
        return render(request,"pages/agregar/varios/add_tipoProducto.html",context)
@login_required
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
            return render(request,"pages/agregar/varios/add_estado.html",context)
    else:
        context = {
            "form":form
        }
        return render(request,"pages/agregar/varios/add_estado.html",context)
@login_required
def add_usuario(request):
    form = UsuarioForm()
    if request.method == "POST":
        nuevo = UsuarioForm(request.POST)
        if nuevo.is_valid():
            usuario_data = nuevo.cleaned_data
            user = User.objects.create_user(
                username=usuario_data["username"],
                password=usuario_data["password"],
            )
            usuario = Usuario(
                user=user,
                rut=usuario_data["rut"],
                id_tipo_usuario=usuario_data["id_tipo_usuario"],
            )
            usuario.save()
            return redirect("Principal")  # redirect to a success page
    context = {
        "form": form
    }
    return render(request, "pages/agregar/varios/add_usuario.html", context)
def del_tipoUser(request,pk):
    try:
        tipoUsuarios = TipoUsuario.objects.get(id_tipo_usuario=pk)
        tipoUsuarios.delete()

        tipoUsuarios = TipoUsuario.objects.all()
        talla = Talla.objects.all()
        tipoBici = TipoBici.objects.all()
        formaPago = FormaPago.objects.all()
        tipoProducto = TipoProducto.objects.all()
        estado = Estado.objects.all()
        context={
            "mensaje":"Registro eliminado exitosamente",
            "tipoUsuarios": tipoUsuarios,
            "talla" : talla,
            "tipoBici" : tipoBici,
            "formaPago" : formaPago,
            "tipoProducto" : tipoProducto,
            "estado" : estado,
        }
        return render(request,"pages/despliegue/crud_varios.html",context)
    except:
        tipoUsuarios = TipoUsuario.objects.all()
        talla = Talla.objects.all()
        tipoBici = TipoBici.objects.all()
        formaPago = FormaPago.objects.all()
        tipoProducto = TipoProducto.objects.all()
        estado = Estado.objects.all()
        context={
            "mensaje":"Error, Datos no encontrados",
            "tipoUsuarios": tipoUsuarios,
            "talla" : talla,
            "tipoBici" : tipoBici,
            "formaPago" : formaPago,
            "tipoProducto" : tipoProducto,
            "estado" : estado,
        }
        return render(request,"pages/despliegue/crud_varios.html",context)
@login_required
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
""" --------------------------------------------------------------------------- """
def loginSession(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "j.riquelmee" and password=="pass1234":
            request.session["user"] = username
            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/despliegue/crud_usuarios.html",context)
        else:
            context ={
                "mensaje":"Usuario o contraseña incorrecta",
                "design" : "alert alert-danger w-50 mx-auto text-center",
            }
            return render(request,"pages/login.html",context)
    else:
        context = {
        }
        return render(request,"pages/login.html",context)

def conectar(request):
    if request.method=="POST":
        #Corresponde al formulario
        username = request.POST["usuario"]
        password = request.POST["pass"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)

            us = Usuario.objects.get(user=user)
            request.session["tipo"] = us.tipo
            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/crud.html",context)
        else:
            context = {
                "mensaje":"Usuario o contraseña incorrecta",
                "design":"alert alert-danger w-50 mx-auto text-center",
            }
            return render(request,"pages/login.html",context)
    else:
        #Corresponde a redireccionar
        context = {
        }
        return render(request,"pages/login.html",context)

def desconectar(request):
    #del request.session["user"]
    if request.user.is_authenticated:
        logout(request)
    context = {
        "mensaje":"Sesion cerrada",
        "design":"alert alert-info w-50 mx-auto text-center",
    }
    return render(request,"pages/login.html",context)