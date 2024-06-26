from django.urls import path
from MasterBikes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crud-varios', views.crud_varios, name='crud-varios'),
    path('crud-usuarios', views.crud_usuarios, name='crud-usuarios'),
]