from django.urls import path
from MasterBikes import views

urlpatterns = [
    path("login", views.conectar, name="login"),
    path("logout", views.desconectar, name="logout"),
    path('crud-varios', views.crud_varios, name='crud-varios'),
    path('crud-usuarios', views.crud_usuarios, name='crud-usuarios'),
    path('crud-arriendos', views.crud_arriendos, name='crud-arriendos'),
    path('crud-reparaciones', views.crud_reparacion, name='crud-reparaciones'),
    path('crud-ventas', views.crud_ventas, name='crud-ventas'),
    path('', views.Principal, name='Principal'),
    path('tienda', views.tienda, name='tienda'),
    path('add-tipo-usuario', views.add_tipoUsuario, name='add-tipo-usuario'),
    path('edit-tipo-usuario/<str:pk>', views.edit_tipoUser, name='edit-tipo-usuario'),
    path('add-talla', views.add_talla, name='add-talla'),
    path('add-bici', views.add_bici, name='add-bici'),
    path('add-forma-pago', views.add_forma_pago, name='add-forma-pago'),
    path('add-tipo-producto', views.add_tipo_producto, name='add-tipo-producto'),
    path('add-estado', views.add_estado, name='add-estado'),
]

""" path('edit-tipo-usuario', views.edit_tipoUsuario, name='edit-tipo-usuario'), """