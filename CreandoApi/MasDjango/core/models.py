from django.db import models


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


class Cliente(models.Model):
    nombre = models.CharField(primary_key=True, max_length=100, verbose_name='Ingrese Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Ingrese Apellido')
    direccion = models.CharField(max_length=200, verbose_name='Ingrese direccion')
    correo = models.EmailField(verbose_name='Ingrese correo electronico')
    telefono = models.CharField(max_length=9, verbose_name='Ingrese numero telefono')

    def __str__(self):

        return self.nombre
