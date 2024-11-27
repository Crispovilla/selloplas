
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('calcular_medidas/', include('calcular_medidas.urls')),
    path('crear_cotizacion/', include('cotizaciones.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
