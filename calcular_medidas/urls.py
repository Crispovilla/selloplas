from django.urls import path
from .views import calcular_medidas, crear_ventana

urlpatterns = [
    path('', calcular_medidas, name='calcular_medidas'), 
    path('crear-ventana/', crear_ventana, name='crear_ventana'),
]