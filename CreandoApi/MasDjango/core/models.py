from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nomCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')

    def __str__(self):

        return self.nomCategoria


class Productos(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id del producto')
    nomProducto = models.CharField(max_length=255, verbose_name='Nombre del producto')
    descripcion = models.TextField(verbose_name='Descripcion del producto')
    precio = models.IntegerField(verbose_name='Precio del producto')
    fechaCreacion = models.DateTimeField(verbose_name='Fecha creacion del producto')
    fechaActualizacion = models.DateTimeField(verbose_name='Fecha de actualizacion del producto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def _str_(self):

        return self.idProducto
    
    def save(self, *args, **kwargs):
        self.clean()  # Llamada a la validación antes de guardar
        super().save(*args, **kwargs)

    def clean(self):
        validate_fecha_actualizacion(self.fechaActualizacion, self)
        validate_fecha_creacion(self.fechaCreacion)

def validate_fecha_creacion(value):
    if value > timezone.now():
        raise ValidationError("La fecha de creación no puede ser en el futuro.")

def validate_fecha_actualizacion(value, instance):
    if value < instance.fechaCreacion:
        raise ValidationError("La fecha de actualización no puede ser anterior a la fecha de creación.")


class Cliente(models.Model):
    nombre = models.CharField(primary_key=True, max_length=100, verbose_name='Ingrese Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Ingrese Apellido')
    direccion = models.CharField(max_length=200, verbose_name='Ingrese direccion')
    correo = models.EmailField(verbose_name='Ingrese correo electronico')
    telefono = models.CharField(max_length=9, verbose_name='Ingrese numero telefono')

    def __str__(self):

        return self.nombre
    
    def clean(self):
        super().clean()
        if not self.telefono.isdigit():
            raise ValidationError("El número de teléfono debe contener solo dígitos.")