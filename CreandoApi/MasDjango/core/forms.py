from django import forms
from django.forms import ModelForm
from .models import Productos

class ProductoForm(ModelForm):

    class Meta:
        model = Productos
        fields = ['idProducto','nomProducto','descripcion','precio','fechaCreacion','fechaActualizacion', 'categoria']