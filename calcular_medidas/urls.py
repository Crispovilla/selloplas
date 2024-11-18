from django.urls import path
from .views import calcular_medidas

urlpatterns = [
    path('', calcular_medidas, name='calcular_medidas'), 
]