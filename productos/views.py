from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings


def index(request):
    return render(request, 'productos/index.html')

def usuario(request):

    datos_usuario = {
        'nombre': 'Emanuel Gutierrez',
        'email': 'emanuel.gutierrez@gmail.com',
        'telefono': '954755903',
        'imagen_url': '/static/productos/img/persona.png',
        'biografia': 'Encargado de la Super Tienda.'
    }

    html_file_path = os.path.join(settings.BASE_DIR, 'productos/templates/productos/usuario.html')

    try:
        with open(html_file_path, 'r') as file:
            html_content = file.read()
    except FileNotFoundError:
        return HttpResponse("<h1>Archivo no encontrado</h1>", status=404)

    html_content = html_content.replace('{{ datos_usuario.nombre }}', datos_usuario['nombre'])
    html_content = html_content.replace('{{ datos_usuario.email }}', datos_usuario['email'])
    html_content = html_content.replace('{{ datos_usuario.telefono }}', datos_usuario['telefono'])
    html_content = html_content.replace('{{ datos_usuario.imagen_url }}', datos_usuario['imagen_url'])
    html_content = html_content.replace('{{ datos_usuario.biografia }}', datos_usuario['biografia'])

    return HttpResponse(html_content)

def productos(request):
    productos_list = [
        {
            'id': 1,
            'nombre': 'Helado savory',
            'descripcion': 'Helado savory sabor chocolate suizo.',
            'precio': 2300,
            'imagen_url': 'productos/img/helado.jpg'
        },
        {
            'id': 2,
            'nombre': 'Papas Fritas congeladas',
            'descripcion': 'Exquisitas papas fritas congeladas.',
            'precio': 6800,
            'imagen_url': 'productos/img/papas.jpg'
        },
        {
            'id': 3,
            'nombre': 'Master Dog',
            'descripcion': 'Alimento para perros.',
            'precio': 22000,
            'imagen_url': 'productos/img/perros.jpg'
        },
        {
            'id': 4,
            'nombre': 'Shampoo Ballerina',
            'descripcion': 'Shampoo con olor a manzanilla.',
            'precio': 1300,
            'imagen_url': 'productos/img/shampoo.jpg'
        }
    ]
    return render(request, 'productos/productos.html', {'productos': productos_list})

def producto_descripcion(request, producto_id):
    productos_list = [
        {
            'id': 1,
            'nombre': 'Helado savory',
            'descripcion': 'Helado savory sabor chocolate suizo.',
            'precio': 2300,
            'imagen_url': 'productos/img/helado.jpg'
        },
        {
            'id': 2,
            'nombre': 'Papas Fritas congeladas',
            'descripcion': 'Exquisitas papas fritas congeladas.',
            'precio': 6800,
            'imagen_url': 'productos/img/papas.jpg'
        },
        {
            'id': 3,
            'nombre': 'Master Dog',
            'descripcion': 'Alimento para perros.',
            'precio': 22000,
            'imagen_url': 'productos/img/perros.jpg'
        },
        {
            'id': 4,
            'nombre': 'Shampoo Ballerina',
            'descripcion': 'Shampoo con olor a manzanilla.',
            'precio': 1300,
            'imagen_url': 'productos/img/shampoo.jpg'
        }
    ]
    producto = next((producto for producto in productos_list if producto['id'] == producto_id), None)
    return render(request, 'productos/descripcion.html', {'producto': producto})
