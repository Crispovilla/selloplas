from django.shortcuts import render

def calcular_medidas(request):
    return render(request, 'calcular_medidas.html')
