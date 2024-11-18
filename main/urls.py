
from django.urls import path
from main.views import index, RegisterUser

urlpatterns = [
    path('', index, name='index'),
    path('registro/', RegisterUser.as_view(), name='register'),
]
