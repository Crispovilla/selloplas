from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PerfilUsuario(models.Model):
    tipos = (
        ('administrador', 'Administrador'),
        ('cliente', 'Cliente')
    )
    tipo = models.CharField(max_length=50, default='cliente', choices=tipos)
    user = models.OneToOneField(User, related_name='perfilusuario', on_delete=models.CASCADE)

    def __str__(self):
        id = self.user.id
        nombre = self.user.first_name
        apellido = self.user.last_name
        usuario = self.user.username
        tipo = self.tipo
        return f'{id} | {nombre} | {apellido} | {usuario} | {tipo}'
