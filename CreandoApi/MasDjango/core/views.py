from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProductoForm
from django.http import HttpResponse
import csv
from .models import Trazabilidad
from tabulate import tabulate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt


def home(request):
    productos = Productos.objects.all()
    datos = {
        'productos': productos
    }

    return render(request, 'core/home.html', datos)


def form_producto(request):

    datos = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)

        if formulario.is_valid:
            formulario.save()

            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'core/form_producto.html', datos)


def form_mod_producto(request, id):
    producto = Productos.objects.get(idProducto=id)

    datos = {
        'form': ProductoForm(instance=producto)
    }

    return render(request, 'core/form_mod_producto.html', datos)


def form_del_producto(request, id):
    producto = Productos.objects.get(idProducto=id)

    producto.delete()

    return redirect(to="home")


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def descargar_informe(request):
    trazabilidades = Trazabilidad.objects.all()

    # Crear una lista de filas de la tabla
    table_rows = []
    for trazabilidad in trazabilidades:
        row = [trazabilidad.producto, trazabilidad.fecha, trazabilidad.cantidad, trazabilidad.accion]
        table_rows.append(row)

    # Crear la tabla con tabulate
    table = tabulate(table_rows, headers=['Producto', 'Fecha', 'Cantidad', 'Acción'], tablefmt='pretty')

    # Crear la respuesta HTTP con el contenido tabulado
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="informe_trazabilidad.txt"'
    response.write(table)

    return response