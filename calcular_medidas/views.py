from django.shortcuts import render
from .services import VentanaAmericana, VentanaEuropeaCorredera, VentanaEuropeaProyectante

def calcular_medidas(request):
    return render(request, 'calcular_medidas.html')

def crear_ventana(request):
    resultado = None
    tipo_ventana_legible = None

    if request.method == 'POST':
        tipo_ventana = request.POST.get('tipo_ventana')
        tipo_ventana_legible = tipo_ventana.replace("_", " ")  # Reemplaza guiones bajos por espacios
        ancho = float(request.POST.get('ancho', 0))
        alto = float(request.POST.get('alto', 0))

        ventana = None
        if tipo_ventana == 'americana':
            ventana = VentanaAmericana(ancho, alto)
            resultado = {
                "Ancho": ventana.ancho,
                "Alto": ventana.alto,
                "Horizontal Móvil": ventana.calcular_horizontal_movil(),
                "Vertical": ventana.calcular_vertical(),
                "Travesaño": ventana.calcular_travesano(),
                "Riel": ventana.calcular_riel(),
                "Refuerzo Travesaño": ventana.calcular_refuerzo_travesano(),
                "Refuerzo Traslapo Móvil": ventana.calcular_refuerzo_traslapo_movil(),
            }
        elif tipo_ventana == 'europea_corredera':
            ventana = VentanaEuropeaCorredera(ancho, alto)
            resultado = {
                "Ancho": ventana.ancho,
                "Alto": ventana.alto,
                "Puerta": ventana.calcular_puerta(),
                "Ventana": ventana.calcular_ventana(),
                "Vertical": ventana.calcular_vertical(),
            }
        elif tipo_ventana == 'europea_proyectante':
            ventana = VentanaEuropeaProyectante(ancho, alto)
            resultado = {
                "Ancho": ventana.ancho,
                "Alto": ventana.alto,
                "Ancho Proyectante": ventana.calcular_ancho_proyectante(),
                "Alto Proyectante": ventana.calcular_alto_proyectante(),
                "Travesaño": ventana.calcular_travesano(),
            }

    return render(request, 'calcular_medidas.html', {
        'resultado': resultado,
        'tipo_ventana': tipo_ventana_legible,
    })
