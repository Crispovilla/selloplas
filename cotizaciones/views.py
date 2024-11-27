from django.shortcuts import render

# Create your views here.
def crear_cotizacion(request):
    datos = {
        'nombre': 'Nombre'
    }
    return render(request, 'crear_cotizacion.html', {'datos': datos})