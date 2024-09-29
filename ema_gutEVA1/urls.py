from django.contrib import admin
from django.urls import path
from productos import views 

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', views.index, name='index'),  
    path('productos/', views.productos, name='productos'),  
    path('usuario/', views.usuario, name='usuario'),  
    path('productos/<int:producto_id>/', views.producto_descripcion, name='producto_descripcion'),
]
