from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuario/', views.usuario, name='usuario'),
    path('productos/', views.productos, name='productos'),
    path('productos/<int:producto_id>/', views.producto_descripcion, name='producto_descripcion'),
]
