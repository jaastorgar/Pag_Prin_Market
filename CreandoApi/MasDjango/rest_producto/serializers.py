from rest_framework import serializers
from core.models import Productos


class ProductoSerializers(serializers.ModelSerializer):

    class Meta:
        model = Productos
        fields = ['idProducto','nomProducto','descripcion','precio','fechaCreacion','fechaActualizacion','categoria']