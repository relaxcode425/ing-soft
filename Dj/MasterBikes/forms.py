from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import TipoUsuario, Usuario, Talla, TipoBici, FormaPago, Arriendo, TipoProducto, Producto, Estado, Reparacion, Pago, Detalle, Despacho

class CustomUserCreationForm(UserCreationForm):
    pass

class TipoUsuarioForm(ModelForm):
    tipo = forms.CharField(max_length=20,
                               required=True)
    descripcion = forms.CharField(max_length=30,
                                  required=True)
    
    class Meta:
        model = TipoUsuario
        fields = ['tipo','descripcion']

class TallaForm(ModelForm):
    talla = forms.CharField(max_length=20,
                               required=True)
    
    class Meta:
        model = Talla
        fields = ['talla']

class BiciForm(ModelForm):
    tipo = forms.CharField(max_length=20,
                               required=True)
    
    class Meta:
        model = TipoBici
        fields = ['tipo']

class FormaPagoForm(ModelForm):
    forma = forms.CharField(max_length=20,
                               required=True)
    
    class Meta:
        model = FormaPago
        fields = ['forma']

class TipoProductoForm(ModelForm):
    tipo = forms.CharField(max_length=20,
                               required=True)
    
    class Meta:
        model = TipoProducto
        fields = ['tipo']

class EstadoForm(ModelForm):
    tipo = forms.CharField(max_length=20,
                               required=True)
    
    class Meta:
        model = Estado
        fields = ['tipo']





        