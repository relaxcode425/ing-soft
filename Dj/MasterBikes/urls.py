from django.urls import path
from MasterBikes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crud-varios', views.crud_varios, name='crud-varios'),
    path('crud-usuarios', views.crud_usuarios, name='crud-usuarios'),
    path('crud-arriendos', views.crud_arriendos, name='crud-arriendos'),
    path('crud-reparaciones', views.crud_reparacion, name='crud-reparaciones'),
    path('crud-ventas', views.crud_ventas, name='crud-ventas'),
    path('Principal', views.Principal, name='Principal'),
]