from django.urls import path
from MasterBikes import views

urlpatterns = [
    path('', views.index, name='index'),
]