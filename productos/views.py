from django.shortcuts import render
from django.http import HttpResponse



# Vista del índice
def index(request):
    return render(request, 'productos/index.html')

# Vista para el usuario/identificación
from django.shortcuts import render

def usuario(request):
    datos_usuario = {
        'nombre': 'Emanuel Gutierrez',
        'email': 'emanuel.gutierrez@gmail.com',
        'telefono': '954755903',
        'imagen_url': 'productos/img/persona.png',
        'biografia': 'Encargado de la Super Tienda.'
    }
    return render(request, 'productos/usuario.html', {'datos_usuario': datos_usuario})

# Vista para la lista de productos
def productos(request):
    productos_list = [
        {
            'id': 1,
            'nombre': 'Producto 1',
            'descripcion': 'Helado savory sabor chocolate suizo.',
            'precio': 2300,
            'imagen_url': 'productos/img/helado.jpg'
        },
        {
            'id': 2,
            'nombre': 'Producto 2',
            'descripcion': 'Exquisitas papas fritas congeladas.',
            'precio': 6800,
            'imagen_url': 'productos/img/papas.jpg'
        },
        {
            'id': 3,
            'nombre': 'Producto 3',
            'descripcion': 'Alimento para perros.',
            'precio': 22000,
            'imagen_url': 'productos/img/perros.jpg'
        },
        {
            'id': 4,
            'nombre': 'Producto 4',
            'descripcion': 'Shampoo con olor a manzanilla.',
            'precio': 1300,
            'imagen_url': 'productos/img/shampoo.jpg'
        }
    ]
    return render(request, 'productos/productos.html', {'productos': productos_list})

# Vista para la descripción del producto
def producto_descripcion(request, producto_id):
    productos_list = [
        {
            'id': 1,
            'nombre': 'Producto 1',
            'descripcion': 'Helado savory sabor chocolate suizo.',
            'precio': 2300,
            'imagen_url': 'productos/img/helado.jpg'
        },
        {
            'id': 2,
            'nombre': 'Producto 2',
            'descripcion': 'Exquisitas papas fritas congeladas.',
            'precio': 6800,
            'imagen_url': 'productos/img/papas.jpg'
        },
        {
            'id': 3,
            'nombre': 'Producto 3',
            'descripcion': 'Alimento para perros.',
            'precio': 22000,
            'imagen_url': 'productos/img/perros.jpg'
        },
        {
            'id': 4,
            'nombre': 'Producto 4',
            'descripcion': 'Shampoo con olor a manzanilla.',
            'precio': 1300,
            'imagen_url': 'productos/img/shampoo.jpg'
        }
    ]
    # Obtener el producto que coincide con el producto_id
    producto = next((producto for producto in productos_list if producto['id'] == producto_id), None)
    return render(request, 'productos/descripcion.html', {'producto': producto})
